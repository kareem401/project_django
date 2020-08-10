from django.db import models


class customer(models.Model):
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name

class product(models.Model):
	CATEGORY = (
		('Indoor', 'Indoor'),
		('Outdoor', 'Outdoor'),
		)
	name = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True)
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	description = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

class order(models.Model):
 	STATUS = (
 		('Pending', 'Pending'),
 		('Out for delivery', 'Out for delivery'),
 		('delivery', 'delivery')
 		)
 	customer = models.ForeignKey(customer, null=True, on_delete=models.SET_NULL)
 	product = models.ForeignKey(product, null=True, on_delete=models.SET_NULL)
 	date_created = models.DateTimeField(auto_now_add=True, null=True)
 	status = models.CharField(max_length=200, null=True, choices=STATUS)

class post(models.Model):
	text =models.TextField(max_length=200, null=True)
	def __str__(self):
		return self.text