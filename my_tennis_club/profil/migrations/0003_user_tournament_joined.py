# Generated by Django 4.2.16 on 2024-11-21 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0002_alter_tournament_id_alter_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='tournament_joined',
            field=models.IntegerField(default=0),
        ),
    ]
