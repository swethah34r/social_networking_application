# Generated by Django 5.0.7 on 2024-07-14 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("v1", "0003_alter_friend_friend_id_alter_friend_user_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="friend",
            name="friend_id",
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name="User",
        ),
    ]