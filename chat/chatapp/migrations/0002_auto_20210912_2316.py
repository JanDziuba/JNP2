# Generated by Django 3.2.5 on 2021-09-12 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='content',
            new_name='message',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='username',
            new_name='user',
        ),
    ]
