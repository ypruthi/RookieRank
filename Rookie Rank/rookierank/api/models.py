from django.db import models
import string
import random
# Create your models here.

def generate_unique_playerID():
    length = 5

    while (True):
        playerID = ''.join(random.choices(string.string.ascii_uppercase, k=length))

        if Player.objects.filter(playerID = playerID).count() == 0:
            break
    return playerID

class Player(models.Model):
    name = models.CharField(max_length = 50, default = "", unique = True)
    playerID = models.CharField(max_length = 5, unique = True)
    sentiment_score = models.DecimalField(max_digits = 5, decimal_places = 4, unique = False)
    created_at=models.DateTimeField(auto_now_add=True)


