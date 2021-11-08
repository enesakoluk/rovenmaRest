from django.db import models
from django.contrib.auth.models import User

class Products(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.TextField()
    categoryId = models.TextField()
    stockInformation = models.IntegerField()
    barcodeNumber = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
