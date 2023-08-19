from django.db import models

class text(models.Model):
    inputText = models.TextField(default="default")