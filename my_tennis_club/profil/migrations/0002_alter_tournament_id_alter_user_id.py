# Generated by Django 4.2.16 on 2024-11-21 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]