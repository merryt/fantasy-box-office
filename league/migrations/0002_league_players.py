# Generated by Django 4.1.3 on 2022-11-18 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_player_nickname"),
        ("league", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="league",
            name="players",
            field=models.ManyToManyField(to="users.player"),
        ),
    ]