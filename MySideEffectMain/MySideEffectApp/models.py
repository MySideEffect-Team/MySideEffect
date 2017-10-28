from django.db import models


class Drug(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    side_effect = models.CharField(max_length=100)
    observed = models.IntegerField()

    sex = models.BooleanField()
    smoker = models.BooleanField()
    alcohol = models.BooleanField()
    pregnant = models.BooleanField()
    weight = models.PositiveSmallIntegerField()



