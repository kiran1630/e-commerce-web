from django.db import models
import datetime
import os
from django.contrib.auth.models import User

def get_filename(request,filename):
    time = datetime.datetime.now().strftime('%Y-%M-%d %H:%M:%S')
    new_file = f'{time}{filename}'
    return os.path.join('uploads/',new_file)

class Category_table(models.Model):
    name = models.CharField(max_length=50,null=False,blank=False)
    image = models.ImageField(upload_to=get_filename,null=True,blank=False)
    description = models.TextField(max_length=500,null=False,blank=False)
    status = models.BooleanField(default=False,help_text='0-show,1-hidden')
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class product_table(models.Model):
    categoty = models.ForeignKey(Category_table,on_delete=models.CASCADE)
    name = models.CharField(max_length=50,null=False,blank=False)
    vendor = models.CharField(max_length=50,null=False,blank=False)
    image = models.ImageField(upload_to=get_filename,null=True,blank=False)
   
    original_price = models.FloatField(null=False,blank=False)
    selling_price = models.FloatField(null=False,blank=False)
    quantity = models.IntegerField(null=False,blank=False)
    description = models.TextField(max_length=500,null=False,blank=False)
    status = models.BooleanField(default=False,help_text='0-show,1-hidden')
    trending = models.BooleanField(default=True,help_text='0-default,1-trending')
    created_at = models.DateTimeField(auto_now_add=True)

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(product_table,on_delete=models.CASCADE)
    product_qty = models.IntegerField(null=False,blank=False)
    created_at =models.DateTimeField(auto_now_add=True)

    @property
    def total_cost(self):
        return self.product_qty*self.product.selling_price

    

