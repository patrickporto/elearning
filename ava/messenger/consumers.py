from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        sending_date = text_data_json['sendingDate']
        logged_user = self.scope['user']

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sending_date': sending_date,
                'author': {
                    'id': logged_user.id,
                    'name': logged_user.username,
                    'photo': 'https://placeimg.com/192/192/people',
                },
            }
        )

    def chat_message(self, event):
        message = event['message']
        sending_date = event['sending_date']
        author = event['author']

        self.send(text_data=json.dumps({
            'message': message,
            'sendingDate': sending_date,
            'author': {
                'me': self.scope['user'].id == author['id'],
                **author
            },
        }))
