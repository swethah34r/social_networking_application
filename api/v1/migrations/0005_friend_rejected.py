# Generated by Django 5.0.7 on 2024-07-14 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("v1", "0004_alter_friend_friend_id_delete_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="friend",
            name="rejected",
            field=models.BooleanField(default=False),
        ),
    ]