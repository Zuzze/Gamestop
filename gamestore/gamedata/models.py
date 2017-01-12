from django.db import models
from developer.models import Developer

class Game(models.Model):
    title = models.CharField(max_length=256, unique=True)
    url = models.URLField(null=False)
    dev = models.ForeignKey(Developer, related_name="games")

    def __unicode__(self):
        return self.title
