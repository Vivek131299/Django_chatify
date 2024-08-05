import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.contrib.auth.models import User

from .models import ChatMessage

from django.utils import timezone


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.user = self.scope['user']
        self.receiver_id = self.scope['url_route']['kwargs']['receiver_id']

        if self.user.id < self.receiver_id:
            self.room_group_name = f"chat_{self.user.id}_{self.receiver_id}"
        else:
            self.room_group_name = f"chat_{self.receiver_id}_{self.user.id}"

        print(self.room_group_name)

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        message = data['message']

        print(message)

        sender = User.objects.get(id=self.user.id)
        receiver = User.objects.get(id=self.receiver_id)
        timestamp = timezone.now()
        print(timezone.now())
        ChatMessage.objects.create(sender=sender, receiver=receiver, message=message, timestamp=timestamp)

        print("In receive: " + self.room_group_name)
        try:
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'chat.message',
                    'message': message,
                    'sender_id': self.user.id,
                    'receiver_id': self.receiver_id,
                    'timestamp': timestamp.isoformat()
                }
            )
        except Exception as e:
            print("Error in receive method: ", str(e))

    # def chat_message(self, event):
    #     message = event['message']
    #
    #     self.send(text_data=json.dumps({
    #         'message': message,
    #         'sender_id': event['sender_id'],
    #         'receiver_id': event['receiver_id']
    #     }))

    # def save_message(self, sender_id, receiver_id, message):
    #     sender = User.objects.get(id=sender_id)
    #     receiver = User.objects.get(id=receiver_id)
    #     ChatMessage.objects.create(sender=sender, receiver=receiver, message=message)

    def chat_message(self, event):
        print("Inside chat_message method")
        self.send(text_data=json.dumps(event))

    def user_join(self, event):
        self.send(text_data=json.dumps(event))

    def user_leave(self, event):
        self.send(text_data=json.dumps(event))

    def private_message(self, event):
        self.send(text_data=json.dumps(event))

    def private_message_delivered(self, event):
        self.send(text_data=json.dumps(event))