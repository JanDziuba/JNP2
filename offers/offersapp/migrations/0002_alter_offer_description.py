# Generated by Django 3.2.5 on 2021-09-05 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offersapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='description',
            field=models.CharField(max_length=400),
        ),
    ]
