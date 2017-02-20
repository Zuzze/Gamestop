from django.db import models
from gamedata.models import Game

class Player(models.Model):
    name = models.CharField(max_length=256, unique=True)
    cart_games = models.ManyToManyField('gamedata.Game', related_name="cart_games", blank=True)

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
            cart_games.remove()
            cart_games.save()

    def player_add_to_cart(self, game_title):
        try:
            game = Game.objects.get(title=game_title)
        except Game.DoesNotExist:
            messages.add_message(request, messages.INFO,
            "Error in cart")
            return HttpResponseRedirect("/error/")
        else:
            #if request.method == 'POST':
                #return HttpResponseRedirect('/dev/')
            #game = get_object_or_404(Game, title=game_title)
            self.cart_games.add(game)
            self.save()
