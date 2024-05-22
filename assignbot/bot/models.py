# assignbot/models.py

from django.db import models

class User(models.Model):
    profile_name = models.CharField(max_length=255,primary_key=True)
    wa_id = models.CharField(max_length=255)
    number = models.CharField(max_length=15)
    def __str__(self):
        return self.profile_name

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default='default_user')
    sms_message_sid = models.CharField(max_length=255, unique=True)
    body = models.TextField()
    replied=models.TextField(default=None)
    sms_status = models.CharField(max_length=50)
    from_number = models.CharField(max_length=15)
    to_number = models.CharField(max_length=15)
    profile_name = models.CharField(max_length=255, null=True)
    media_url = models.URLField(null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body + self.from_number
