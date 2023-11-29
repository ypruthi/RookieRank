from django.db import models
import string
import random

# Create your models here.

def generate_unique_name():
    length = 5

    while (True):
        name = ''.join(random.choices(string.ascii_uppercase, k=length))

        if RankRoom.objects.filter(name = name).count() == 0:
            break
    return name

class RankRoom(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 50, default = generate_unique_name, unique = True)
    host = models.CharField(max_length=50, unique=True, default="")
    number_of_players = models.IntegerField(null=False, default=1)
    choose_players = models.BooleanField(null=False, default=False)
    created_at=models.DateTimeField(auto_now_add=True)


