from django.db import models
from gamedata.models import Game

class Player(models.Model):
    name = models.CharField(max_length=256, unique=True)

    def __unicode__(self):
        return self.name

    def player_add_game(self, game_title):
        try:
            game = Game.objects.get(title=game_title)
        except Game.DoesNotExist:
            return None
        else:
            game.players.add(self)
            game.save()

    def player_add_to_cart(self, game_title):
        try:
            game = Game.objects.get(title=game_title)
        except Game.DoesNotExist:
            return None
        else:
            game.players.add(self)
            game.save()
