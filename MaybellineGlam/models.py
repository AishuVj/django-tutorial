from django.db import models #importing models from django.db


# Create a class Maybelline that inherits from models.Models
class Maybelline(models.Model):
    
    #Creating fieldnames with respective datatype(CharField,FloatField,TextField) that takes max_length(specifices the length of the characters) and null parameter(Specifies if it can accept empty field values)
    brand = models.CharField(max_length=15,null=True)
    name = models.CharField(max_length=150,null=True)
    price = models.FloatField(null=True)
    image_link = models.CharField(max_length=255,null=True)
    product_link = models.CharField(max_length=255,null=True)
    website_link = models.CharField(max_length=255,null=True)
    description = models.TextField(null=True)
    rating = models.FloatField(null=True)
    category = models.CharField(max_length=15,null=True)
    product_type = models.CharField(max_length=20,null=True)
    colour_name = models.CharField(max_length=255,null=True)

    
    

    





    
   