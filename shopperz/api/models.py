from django.db import models

# Create your models here.

class User(models.Model):
    firstname = models.CharField(max_length=120)
    lastname = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=120)
    phonenumber = models.CharField(max_length=120)
    isShopper = models.BooleanField(default=False)
    
    def __str__(self):
        return "{} - {}".format(self.firstname, self.email)
    
