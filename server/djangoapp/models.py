from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib import admin
import datetime
#from .models import CarMake, CarModel

# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object

class CarMake(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    founded_year = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.founded_year})"

# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many
# Car Models, using ForeignKey field)
# - Name
# - Type (CharField with a choices argument to provide limited choices
# such as Sedan, SUV, WAGON, etc.)
# - Year (IntegerField) with min value 2015 and max value 2023
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object

class CarModel(models.Model):
    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'Wagon'
    TRUCK = 'Truck'
    COUPE = 'Coupe'
    CONVERTIBLE = 'Convertible'
    
    CAR_TYPES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
        (TRUCK, 'Truck'),
        (COUPE, 'Coupe'),
        (CONVERTIBLE, 'Convertible'),
    ]

    make = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name='models')
    dealer_id = models.IntegerField()
    name = models.CharField(max_length=100)
    car_type = models.CharField(max_length=20, choices=CAR_TYPES)
    year = models.DateField(default=datetime.date.today)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    horsepower = models.PositiveIntegerField(blank=True, null=True)
    fuel_type = models.CharField(max_length=50, blank=True, null=True)
    transmission = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.make.name} {self.name} ({self.year.year}) - {self.car_type}"
    
    # Registering models with their respective admins
#admin.site.register(CarMake)
#admin.site.register(CarModel)
