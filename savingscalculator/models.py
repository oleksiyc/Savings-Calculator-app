from django.db import models

# Create your models here.

class Calculator(models.Model):
	initial_capital = models.CharField(max_length=50)
	number_of_years = models.CharField(max_length=50)
	interest_rate = models.CharField(max_length=50)
	final_capital = models.CharField(max_length=50)
