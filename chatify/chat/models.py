from django.contrib.auth.models import User
from django.db import models


class Request(models.Model):
    request_sent_from = models.ForeignKey(User, related_name="sent_requests", on_delete=models.CASCADE)
    request_sent_to = models.ForeignKey(User, related_name="received_requests", on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return f'Request from {self.request_sent_from} to {self.request_sent_to}, accepted: {self.accepted}'
