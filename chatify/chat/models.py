from django.contrib.auth.models import User
from django.db import models


class Request(models.Model):
    request_sent_from = models.ForeignKey(User, related_name="sent_requests", on_delete=models.CASCADE)
    request_sent_to = models.ForeignKey(User, related_name="received_requests", on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return f'Request from {self.request_sent_from} to {self.request_sent_to}, accepted: {self.accepted}'


class ChatMessage(models.Model):
    sender = models.ForeignKey(User, related_name="sent_messages", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="received_messages", on_delete=models.CASCADE)
    message = models.TextField(max_length=1000)
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"Message: {self.message} ; sender: {self.sender} ; receiver: {self.receiver} ; timestamp: {self.timestamp}"
