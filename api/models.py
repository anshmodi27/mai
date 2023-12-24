from django.db import models

# Create your models here.

class Category(models.Model):
    categoryName = models.CharField(max_length=500)
    categoryLink = models.CharField(max_length=500, default='', blank=True, null=True)
   

    def __str__(self):
        return self.categoryName
    

class Product(models.Model):
    productName = models.CharField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    productLink = models.CharField(max_length=500, default='', blank=True, null=True)  
    packing = models.CharField(max_length=50)     
    crop = models.CharField(max_length=500)
    description = models.TextField(default='', blank=True, null=True)
    listdes = models.JSONField(default=list,blank=True, null=True)
    images = models.ImageField(upload_to='images/')
    isLive = models.BooleanField(default=False)
    isLatest = models.BooleanField(default=False)
    isHot = models.BooleanField(default=False)
    isDeleted = models.BooleanField(default=False)
    
    

    def __str__(self):
        return self.productName
    

class Inquiry(models.Model):
    firstName = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    lastName = models.CharField(max_length=100, default='', blank=True, null=True)  
    contectno = models.CharField(max_length=20)   
    email = models.EmailField(max_length=100)  
    selected_category = models.CharField(max_length=50)
    selected_product = models.CharField(max_length=50)
    description = models.TextField(default='', blank=True, null=True)
    date = models.DateTimeField(auto_now=True)
    time = models.TimeField(auto_now=True)
   
    
    

    def __str__(self):
        return self.firstName   

