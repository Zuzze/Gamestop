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

    def modify_game(self, game, game_title_=None, game_url_=None, game_des_=None,
                    game_icon_=None, game_price_=None, game_category_=None):
        print("Modifying game")
        if (game_title_):
            game.title = game_title_;
        if (game_url_):
            game.url = game_url_;
        if (game_des_):
            game.description = game_des_;
        if (game_icon_):
            game.icon = game_icon_;
        if (game_price_):
            game.price = game_price_;
        if (game_category_):
            game.category = game_category_;
        game.save();

    def __unicode__(self):
        return self.name
