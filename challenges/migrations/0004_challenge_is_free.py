# Generated by Django 5.0.7 on 2024-08-05 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0003_challenge_secret_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='is_free',
            field=models.BooleanField(default=False),
        ),
    ]
