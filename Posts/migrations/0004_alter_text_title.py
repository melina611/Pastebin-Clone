# Generated by Django 4.2.4 on 2023-08-24 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0003_text_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='text',
            name='title',
            field=models.CharField(default='Title', max_length=150),
        ),
    ]
