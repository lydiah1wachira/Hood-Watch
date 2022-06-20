from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
import cloudinary
from cloudinary.models import CloudinaryField


# Create your models here.
class Neighbourhood(models.Model):
   
    name=models.CharField(max_length=60, null=True)
    description=models.CharField(max_length=400, null=True)
    location=models.CharField(max_length=200, null=True)
    population=models.IntegerField()
    image = CloudinaryField( null = True, blank = True)

    def __str__(self):
        return self.name

    def create_neigbourhood(self):
        self.save()

    def delete_neigbourhood(self):
        self.delete()

    @classmethod
    def find_neighbourhood(cls,id):
        neighbourhood = cls.objects.get(id=id)
        return neighbourhood

    def update_neighbourhood(self,name):
        self.name = name
        self.save()


    def __str__(self):
        return f'{self.name}'