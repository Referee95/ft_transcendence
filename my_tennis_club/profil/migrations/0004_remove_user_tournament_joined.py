# Generated by Django 4.2.16 on 2024-11-21 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0003_user_tournament_joined'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='tournament_joined',
        ),
    ]