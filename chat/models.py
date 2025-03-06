from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    text = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} -> {self.receiver} at {self.timestamp}"

class Attachment(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='attachments')
    file = models.FileField(upload_to='chat_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Attachment for Message ID {self.message.id}"
