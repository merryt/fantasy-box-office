# Generated by Django 2.2.28 on 2023-04-18 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0002_rename_players_league_teams_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='league',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='team',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]