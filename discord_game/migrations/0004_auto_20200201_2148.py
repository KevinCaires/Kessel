# Generated by Django 2.1.10 on 2020-02-01 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('discord_game', '0003_auto_20200201_2137'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='actual_area',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='discord_game.Area'),
        ),
        migrations.AddField(
            model_name='profile',
            name='actual_zone',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='discord_game.Zone'),
        ),
        migrations.AddField(
            model_name='zone',
            name='areas',
            field=models.ManyToManyField(to='discord_game.Area'),
        ),
    ]