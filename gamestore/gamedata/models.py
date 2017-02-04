from django.db import models

class Game(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256, unique=True)
    url = models.URLField(null=False)
    dev = models.ForeignKey('developer.Developer', related_name="games")
    players = models.ManyToManyField('player.Player', related_name="games")
    description = models.CharField(max_length=1024, null=True, blank=True)
    icon = models.URLField(null=True, blank=True)
    price = models.DecimalField(null=False, max_digits=8, default=5.0, decimal_places=2)

    def __unicode__(self):
        return self.title

    #def add_player(self, player_):
    #    self.player
