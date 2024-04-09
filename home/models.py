from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    phone=models.CharField(max_length=122)
    email=models.CharField(max_length=12)
    desc=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name


class Maintenance(models.Model):
    name=models.CharField(max_length=122)
    phone=models.CharField(max_length=122)
    email=models.CharField(max_length=12)
    date=models.DateField()

    def __str__(self):
        return self.name


class Driving(models.Model):
    name = models.CharField(max_length=122)
    dob = models.DateField()
    address = models.TextField()
    model = models.CharField(max_length=122)
    type = models.CharField(max_length=20)
    pic = models.ImageField(upload_to='license_photos/')
    date=models.DateField()

    def __str__(self):
        return self.name
    
    
class Olas1pro(models.Model):
    name = models.CharField(max_length=122)
    
    email=models.CharField(max_length=112)
    address = models.TextField()
    brandname = models.CharField(max_length=20 ,null=True)
    # model = models.CharField(max_length=122)
    
    date=models.DateField()

    def __str__(self):
        return self.brandname



class Tvswarranty(models.Model):
    name=models.CharField(max_length=122)
    phone=models.CharField(max_length=122)
    email=models.CharField(max_length=112)
    brandname = models.CharField(max_length=20 ,null=True)
    date=models.DateField()


    def __str__(self):
        if self.brandname is not None:
            return self.brandname
        else:
            return "No Brand"
    
