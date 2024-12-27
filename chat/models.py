from django.db import models
from django.core.files.storage import FileSystemStorage

class Message(models.Model):
    name = models.CharField(max_length=50)  # User's name
    content = models.TextField()  # Chat message content
    timestamp = models.DateTimeField(auto_now_add=True)  # Time of message creation
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, storage=FileSystemStorage())

    def __str__(self):
        return f"{self.name}: {self.content[:20]}..."  # Short preview of the message

class IPLog(models.Model):
    ip_address = models.GenericIPAddressField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ip_address} at {self.timestamp}"