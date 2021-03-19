from django.db import models

# Create your models here.
class pizzas(models.Model):

	name = models.CharField(max_length=25)

	img = models.ImageField()

class drink(models.Model):

	name = models.CharField(max_length=25)

	img = models.ImageField()

class burger(models.Model):
	name = models.CharField(max_length=25)

	img = models.ImageField()



class pasta(models.Model):

	name = models.CharField(max_length=25)

	img = models.ImageField()


class order(models.Model):

	name = models.CharField(max_length=25)

	inte = models.IntegerField()
	