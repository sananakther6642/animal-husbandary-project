# from django.db import models


# # Create your models here.

from enum import unique
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import AutoField, CharField, DateTimeField, EmailField


# Create your models here.

class staff(models.Model):
    staffID = models.IntegerField(primary_key=True)
    staffName = models.CharField(max_length=30)
    Address = models.TextField()
    phone = models.BigIntegerField()
    designation = models.CharField(max_length=10)
    dateofjoin = models.DateField()

    def __str__(self):
        return self.staffName


class customer(models.Model):

    customerID = models.AutoField(primary_key=True)
    CustomerName = models.CharField(max_length=30)
    phoneNo = models.BigIntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=45)
    Address = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    state = models.CharField(max_length=45)
    pincode = models.CharField(max_length=45)

    def __str__(self):
        return self.CustomerName

    def __int__(self):
        return self.customerID


class animal(models.Model):

    animalID = models.IntegerField(primary_key=True)
    typeofanimal = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    price = models.IntegerField()

    status = models.CharField(max_length=30)
    stf = models.ForeignKey(staff, on_delete=models.CASCADE)
    order = models.ManyToManyField(customer)

    def __int__(self):
        return self.animalID

    def __int__(self):
        return self.order


class vaccine(models.Model):

    vaccineID = models.IntegerField(primary_key=True)
    animalID = models.IntegerField()
    remark = models.CharField(max_length=30)
    date_of_vaccination = models.DateField()
    vaccinated = models.ManyToManyField(animal)

    def __int__(self):
        return self.vaccineID

    def __int__(self):
        return self.animalID

    class Meta:
        unique_together = (('vaccineID', 'animalID'))




class food(models.Model):
    foodID = models.IntegerField(primary_key=True)
    animalID = models.ForeignKey(animal, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    quantity = models.IntegerField()
    fooditem = models.TextField()

    def __str__(self):
        return self.fooditem

    def __int__(self):
        return self.animalID



class staflog(models.Model):

    email = models.EmailField()
    password = CharField(max_length=25)

    def __str__(self):
        return self.email


class feedback(models.Model):
    cname = models.TextField()
    email = models.EmailField()
    suggestion = models.TextField()
    improvements = models.TextField()

    def __str__(self):
        return self.cname
