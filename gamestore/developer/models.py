from django.db import models

class Developer(models.Model):
    name = models.CharField(max_length=256, unique=True)

    def __unicode__(self):
        return self.name
