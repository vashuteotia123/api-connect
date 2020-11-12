from django.db import models

# Create your models here.

class Reviews(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100,null=True)
    restaurant_name = models.CharField(max_length=100,null=True)
    feedback = models.CharField(max_length=2000,null=True)
    rating = models.CharField(max_length=100,null=True)
