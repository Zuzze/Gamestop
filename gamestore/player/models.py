from django.db import models
from gamedata.models import Game

class Player(models.Model):
    name = models.CharField(max_length=256, unique=True)

    def __unicode__(self):
        return self.name
