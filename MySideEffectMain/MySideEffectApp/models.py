from django.db import models


class Occurence(models.Model):
    # Lists
    adverse_effects = models.TextField(
        null=True, blank=True

    )
    drug_names = models.TextField(
        null=True, blank=True
    )


    # Other fields
    age = models.PositiveSmallIntegerField(
        null=True, blank=True

    )
    weight = models.FloatField(
        null=True, blank=True
    )

    gender = models.CharField(
        max_length=30,
        null=True, blank=True
    )

    continent = models.CharField(
        max_length=30, null=True, blank=True
    )

    literature_reference = models.CharField(
        max_length=100, null=True, blank=True
    )
