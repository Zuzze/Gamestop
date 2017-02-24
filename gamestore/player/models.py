from django.db import models
from gamedata.models import Game
from django.contrib.auth.models import User

class Player(models.Model):
    user = models.ForeignKey(User)
    cart_games = models.ManyToManyField('gamedata.Game', related_name="cart_games", blank=True)

    def __unicode__(self):
        return self.name

    def player_add_game(self):
        for game in self.cart_games.all():
            """ Check if player has already bought the game """
            try:
                player_game = self.games.get(title=game.title)
            except Game.DoesNotExist:
                try:
                    game_ = Game.objects.get(title=game.title)
                except Game.DoesNotExist:
                    continue
                else:
                    game_.players.add(self)
                    game_.save()
                    PlayerGameData(player=self, game=game_).save()
                    #self.cart_games.remove()
                    #self.cart_games.save()

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
