from channels.generic.websocket import AsyncWebsocketConsumer
import json


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        logged_user = self.scope['user']

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_event",
                "event_type": "chat_connect",
                'author': {
                    'id': logged_user.id,
                    'name': logged_user.nome,
                    'photo': logged_user.foto.url,
                },
            }
        )

    async def disconnect(self, close_code):
        logged_user = self.scope['user']
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_event",
                "event_type": "chat_disconnect",
                'author': {
                    'id': logged_user.id,
                    'name': logged_user.nome,
                    'photo': logged_user.foto.url,
                },
            }
        )
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        sending_date = text_data_json['sendingDate']
        logged_user = self.scope['user']
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sending_date': sending_date,
                'author': {
                    'id': logged_user.id,
                    'name': logged_user.nome,
                    'photo': logged_user.foto.url,
                },
            }
        )

    async def chat_message(self, event):
        message = event['message']
        sending_date = event['sending_date']
        author = event['author']

        await self.send(text_data=json.dumps({
            'type': 'chat_message',
            'message': message,
            'sendingDate': sending_date,
            'author': {
                'me': self.scope['user'].id == author['id'],
                **author
            },
        }))

    async def chat_event(self, event):
        event_type = event['event_type']
        author = event['author']

        await self.send(text_data=json.dumps({
            'type': event_type,
            'author': author,
        }))
