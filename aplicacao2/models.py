from django.db import models

# Create your models here.
class Carro(models.Model):
	nmcarro = models.CharField(max_length=50)
	marca = models.CharField(max_length=20)
	data = models.DateTimeField()

