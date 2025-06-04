from django.db import models

# Create your models here.
class Type(models.Model):
    title = models.CharField(max_length=20)
    code = models.CharField(max_length=15,default='tshirt')
    def __str__(self):
        return self.title
    
class Tag(models.Model):
    title = models.CharField(max_length=20)
    def __str__(self):
        return self.title
    
class Color(models.Model):
    title = models.CharField(max_length=20)
    def __str__(self):
        return self.title
    
class Designer(models.Model):
    des_name = models.CharField(max_length=30,default='Unknown')
    def __str__(self):
        return self.des_name

class Product(models.Model):
    name = models.CharField(max_length=100)
    disc = models.TextField()
    prod_type = models.ForeignKey('Type',null=True, on_delete=models.SET_NULL)
    GENDER_CHOICES = [
        ('M','MALE'),
        ('F','FEMALE'),
        ('U','UNISEX')
    ]
    gender = models.CharField(choices=GENDER_CHOICES, default='U')
    stock = models.IntegerField(default=0)
    tags = models.ManyToManyField('Tag')
    SIZE_CHOICES = [
        ('S','S'),
        ('M','M'),
        ('L','L'),
        ('XL','XL'),
        ('XXL','XXL'),
        ('XXXL','XXXL')
    ]
    size = models.CharField(choices=SIZE_CHOICES, default='S')
    colors = models.ForeignKey('Color', on_delete=models.SET_NULL, null=True)
    img_url = models.CharField(max_length=200,null=True)
    price = models.IntegerField(default=0)
    by = models.ForeignKey('Designer',default=1, on_delete=models.CASCADE)
    def  __str__(self):
        return self.name
