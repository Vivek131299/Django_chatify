from django.contrib import admin
from .models import Request, ChatMessage

# Register your models here.
admin.site.register(Request)
admin.site.register(ChatMessage)
