from django.db import models
from gamedata.models import Game

class Developer(models.Model):
    name = models.CharField(max_length=256, unique=True)

    def add_game(self, title, url, price=None, desc=None, icon=None):
        game = Game(title=title, url=url, dev=self, description=desc,
        icon=icon, price=price)
        game.save()

    def __unicode__(self):
        return self.name
