from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=256, unique=True)
    url = models.URLField(null=False)
    dev = models.ForeignKey('developer.Developer', related_name="games")
    player = models.ForeignKey('player.Player', related_name="games", null=True, blank=True)

    def __unicode__(self):
        return self.title
