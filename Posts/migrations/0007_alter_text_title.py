# Generated by Django 4.2.4 on 2023-08-24 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0006_alter_text_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='text',
            name='title',
            field=models.CharField(default='Default Title', max_length=100),
        ),
    ]