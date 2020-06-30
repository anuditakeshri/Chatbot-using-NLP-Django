from django.db import models

# Create your models here.
class messageItem(models.Model):
    content = models.TextField()
    isbot = models.BooleanField(default = False)
    