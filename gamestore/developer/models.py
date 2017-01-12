from django.db import models
from gamedata.models import Game

class Developer(models.Model):
    name = models.CharField(max_length=256, unique=True)

    def add_game(self, title, url):
        game = Game(title=title, url=url, dev=self)

    def __unicode__(self):
        return self.name
