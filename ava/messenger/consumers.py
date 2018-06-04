from channels.generic.websocket import AsyncWebsocketConsumer
import json
from .models import Mensagem, Curtida, Duvida


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        logged_user = self.scope['user']

        await self.channel_layer.group_add(
            self.room_name,
            self.channel_name
        )
        await self.accept()
        for mensagem in Mensagem.objects.filter(turma=self.room_name).order_by('data_publicacao'):
            await self.send(text_data=json.dumps({
                'type': mensagem.tipo,
                'id': mensagem.id,
                'message': mensagem.conteudo,
                'sendingDate': mensagem.data_publicacao.isoformat(),
                'likes': mensagem.curtidas.count(),
                'author': {
                    'me': self.scope['user'].id == mensagem.autor.id,
                    'id': mensagem.autor.id,
                    'name': mensagem.autor.nome,
                    'photo': mensagem.autor.foto.url,
                },
            }))
            
        await self.channel_layer.group_send(
            self.room_name,
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
            self.room_name,
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
            self.room_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        event_type = text_data_json['type']
        if event_type == 'chat_message':
            await self.receive_chat_message(text_data_json)
        elif event_type == 'chat_like':
            await self.receive_chat_like(text_data_json)
        elif event_type == 'chat_add_question':
            await self.receive_chat_add_question(text_data_json)
    
    async def receive_chat_message(self, text_data_json):
        message = text_data_json['message']
        sending_date = text_data_json['sendingDate']
        logged_user = self.scope['user']

        mensagem = Mensagem.objects.create(
            turma_id=int(self.room_name),
            autor=logged_user,
            conteudo=message,
        )
        await self.channel_layer.group_send(
            self.room_name,
            {
                'type': 'chat_message',
                'id': mensagem.id,
                'message': message,
                'likes': 0,
                'sending_date': sending_date,
                'author': {
                    'id': logged_user.id,
                    'name': logged_user.nome,
                    'photo': logged_user.foto.url,
                },
            }
        )
    
    async def receive_chat_like(self, text_data_json):
        message_id = text_data_json['messageId']
        logged_user = self.scope['user']
        try:
            Curtida.objects.get(mensagem_id=int(message_id), autor=logged_user).delete()
            likes = -1
        except Curtida.DoesNotExist:
            Curtida.objects.create(
                mensagem_id=int(message_id),
                autor=logged_user,
            )
            likes = 1
        await self.channel_layer.group_send(
            self.room_name,
            {
                'type': 'chat_like',
                'message_id': message_id,
                'likes': likes,
                'author': {
                    'id': logged_user.id,
                    'name': logged_user.nome,
                    'photo': logged_user.foto.url,
                },
            }
        )

    async def receive_chat_add_question(self, text_data_json):
        message_id = text_data_json['messageId']
        Duvida.objects.get_or_create(
            mensagem_id=int(message_id),
            turma_id=int(self.room_name),
        )

    async def chat_message(self, event):
        message = event['message']
        sending_date = event['sending_date']
        author = event['author']
        message_id = event['id']
        likes = event['likes']

        await self.send(text_data=json.dumps({
            'type': 'chat_message',
            'id': message_id,
            'message': message,
            'likes': likes,
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

    async def chat_like(self, event):
        author = event['author']
        message_id = event['message_id']
        likes = event['likes']

        await self.send(text_data=json.dumps({
            'type': 'chat_like',
            'author': author,
            'likes': likes,
            'messageId': message_id,
        }))

    async def duvidas(self, event):
        await self.send(text_data=json.dumps(event))
