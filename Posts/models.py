from django.db import models

class text(models.Model):
    title = models.CharField(max_length=150, default="difaultTitle")
    inputText = models.TextField(default="default")