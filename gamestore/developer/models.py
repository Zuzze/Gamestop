from django.db import models
from gamedata.models import Game
from django.contrib.auth.models import User

class Developer(models.Model):
    user = models.ForeignKey(User)
    registered = models.BooleanField(default=False)
    activation_key = models.CharField(max_length=32, default="")

    def add_game(self, title, url, price=None, desc=None, icon=None, category='O'):
        game = Game(title=title, url=url, dev=self, description=desc,
        icon=icon, price=price, category=category)
        game.save()

    def __unicode__(self):
        return self.name
