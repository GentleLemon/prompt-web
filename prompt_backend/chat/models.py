from django.db import models
from django.contrib.auth.models import User


class Conversation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    message = models.TextField()
    messages = models.TextField(default='')
    tokens = models.IntegerField(default=0)
    is_bot = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Prompt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField(null=True, blank=True)
    prompt = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Setting(models.Model):
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
