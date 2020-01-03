from django.db import models

# Create your models here.

#the parameter models.Model is used to inherit from the 'models' class
class Product(models.Model):

	#these variables are mapped to the data base with the value of the
	#method on 'models'
	title 		= models.CharField(max_length=120) # this is a required field and django will throw up an error if it's not specified
	description = models.TextField(blank=True, null=True)
	price 		= models.DecimalField(decimal_places=2, max_digits=10)
	summary		= models.TextField(blank=False, null=False) # blank has to do with how the field is rendered, null has to do with the database
	featured 	= models.BooleanField()


