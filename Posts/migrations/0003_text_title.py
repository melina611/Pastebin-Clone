# Generated by Django 4.2.4 on 2023-08-21 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0002_text_inputtext'),
    ]

    operations = [
        migrations.AddField(
            model_name='text',
            name='title',
            field=models.CharField(default='difaultTitle', max_length=150),
        ),
    ]