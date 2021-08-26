# Generated by Django 3.2.5 on 2021-08-23 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('size', models.DecimalField(decimal_places=2, max_digits=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('description', models.CharField(max_length=200)),
                ('seller_username', models.CharField(max_length=20)),
                ('seller_id', models.IntegerField()),
            ],
        ),
    ]