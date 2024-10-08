# Generated by Django 4.0.6 on 2024-10-07 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0006_alter_result_user_choices'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='user_choices',
        ),
        migrations.AddField(
            model_name='result',
            name='user_choices_json',
            field=models.JSONField(default=dict),
        ),
    ]