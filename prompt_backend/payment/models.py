from django.db import models

class Package(models.Model):
    price = models.DecimalField(max_digits=5, decimal_places=2)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
