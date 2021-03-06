from django.db import models
from gamedata.models import Game
from django.contrib.auth.models import User

from django.utils import timezone
from datetime import datetime

secret_key = "1cb99704bf0d36de9d83a740009c37de";

class Player(models.Model):
    user = models.ForeignKey(User)
    registered = models.BooleanField(default=False)
    activation_key = models.CharField(max_length=32, default="")
    cart_games = models.ManyToManyField('gamedata.Game', related_name="cart_games", blank=True)

    def __unicode__(self):
        return self.name

    def player_add_game(self):
        """ Check if player has already bought the game """
        for game in self.cart_games.all():
            try:
                player_game = self.games.get(id=game.id)
            except Game.DoesNotExist:
                try:
                    game_ = Game.objects.get(id=game.id)
                except Game.DoesNotExist:
                    continue
                else:
                    """ Add cart games and remove from cart """
                    game_.players.add(self)
                    game_.last_purchased = timezone.now()
                    game.last_purchased
                    game_.save()
                    print("Game purchased on {0}".format(game_.last_purchased))
                    PlayerGameData(player=self, game=game_).save()
                    self.cart_games.remove(game_)
                    self.save()
            else:
                self.cart_games.remove(player_game)
                self.save()

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

class PlayerGameData(models.Model):
    player = models.ForeignKey('Player', related_name='game_data')
    game = models.ForeignKey('gamedata.Game')
    player_high_score = models.DecimalField(null=True, max_digits=16,
                        default=0, decimal_places=2)
    game_save_data = models.CharField(max_length=4096, null=True)

    def update_game_data(self, data):
        #print(data)
        if (data['messageType'] == 'SCORE'):
            score = int(data['score'])
            if self.player_high_score < score:
                print("Update personal score")
                self.player_high_score = score
                self.save()
            if self.game.highest_score < score:
                print("Update highest score")
                self.game.highest_score = score
                self.game.save()
        elif (data['messageType'] == 'SAVE'):
            self.game_save_data = data['state']
            self.save()

    def get_game_data(self, gameId):
        pass
