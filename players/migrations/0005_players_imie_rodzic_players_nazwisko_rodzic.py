# Generated by Django 4.0.1 on 2022-01-30 19:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0004_remove_players_lp_alter_players_bieg_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='players',
            name='imie_rodzic',
            field=models.CharField(default=django.utils.timezone.now, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='players',
            name='nazwisko_rodzic',
            field=models.CharField(default=django.utils.timezone.now, max_length=40),
            preserve_default=False,
        ),
    ]
