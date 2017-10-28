from django.db import models


class Drug(models.Model):
    name = models.CharField(max_length=100)
    side_effect = models.CharField(max_length=100)
    observed = models.IntegerField()
