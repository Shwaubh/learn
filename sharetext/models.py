from django.db import models
from django.contrib.auth.models import User


class Data(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    msg = models.CharField(max_length=200)
    file = models.FileField(null=True)

    def __str__(self):
        return self.sender.username + "__" + self.receiver.username
