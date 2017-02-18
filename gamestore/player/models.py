from django.db import models
from gamedata.models import Game

class Player(models.Model):
    name = models.CharField(max_length=256, unique=True)
    #cart_games = models.ForeignKey('gamedata.Game', related_name="cart_games")

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

            def add_game(self, title, url, price=None, desc=None, icon=None):
                game = Game(title=title, url=url, dev=self, description=desc,
                icon=icon, price=price)
                game.save()

    def player_add_to_cart(self, game_id):
        try:
            game = Game.objects.get(id=game_id)
        except Game.DoesNotExist:
            return None
        #else:
            #self.cart_games.add(game_id)
            #self.save()
