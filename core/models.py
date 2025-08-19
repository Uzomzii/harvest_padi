from django.db import models

class FarmerProfile(models.Model):
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120, blank=True)
    crops = models.CharField(max_length=200, blank=True)  # e.g., "tomato, pepper"
    about = models.TextField(blank=True)

    def __str__(self):
        return self.name
