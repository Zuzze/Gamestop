from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone

class Game(models.Model):
    GameCategory = (('A', 'Action'), ('RP', 'Role Playing'), ('FPS', 'FPS'), ('SM', 'Simulation'),
                    ('SR', 'Stratergy'), ('O', 'Other'))
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256, unique=True)
    url = models.URLField(null=False)
    dev = models.ForeignKey('developer.Developer', related_name="games")
    players = models.ManyToManyField('player.Player', related_name="games")
    category = models.CharField(choices=GameCategory, max_length=8, default='S')
    description = models.CharField(max_length=1024, null=True, blank=True)
    icon = models.URLField(null=True, blank=True)
    price = models.DecimalField(null=False, max_digits=8, default=5.0, decimal_places=2)
    highest_score = models.DecimalField(null=True, max_digits=16, default=0, decimal_places=2)
    added = models.DateTimeField(auto_now_add=True)
    last_purchased = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.title
