from django.db import models
# Create your models here.


# class User(models.Model):
#     id = models.AutoField(primary_key=True)
#     email = models.CharField(max_length=255)
#     name = models.CharField(max_length=100)
#     password = models.CharField(max_length=255)


class Friend(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    friend_id = models.IntegerField()
    requested = models.BooleanField(default=True)
    validated = models.BooleanField(default=False)
    rejected = models.BooleanField(default=False)
