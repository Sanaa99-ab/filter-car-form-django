

# Create your models here.
# polls/models.py

from django.db import models


class Car(models.Model):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    annee = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Define a DecimalField for the price
    #delay = models.IntegerField()
    car_image = models.ImageField(blank=True, null=True, upload_to='car_images/')

    def __str__(self):
        return f"{self.marque} {self.modele} ({self.annee}) - Price: {self.price}"

    
    # Other fields related to a car
    class Meta:
        app_label = 'polls'
# polls/models.py

