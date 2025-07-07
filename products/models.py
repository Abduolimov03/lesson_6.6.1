from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='car-images/', blank=True, null=True, default='default/car.png')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.model