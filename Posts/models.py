from django.db import models

class Text(models.Model):
    title = models.CharField(max_length=150, default='Default Title')       
    inputText = models.TextField(default="default") 