from django.db import models
import re

class Item(models.Model):
    ITEM_CHOICES = (('caps', 'Caps'), ('coats', 'Coats'), ('hats', 'Hats'), ('hoodies', 'Hoodies'), ('jackets', 'Jackets'), 
                    ('jackets', 'Jackets'), ('shirts', 'Shirts'), ('skits', 'Skirts'), ('sweaters', 'Sweaters'), 
                    ('waistcoats', 'Waistcoats'), ('specials', 'Specials'))

    item_Type = models.CharField(max_length=30, choices=ITEM_CHOICES, default='caps')
    item_Name = models.CharField(max_length=100)
    
    item_Image = models.ImageField(upload_to='static/img/collections')
    item_Price = models.FloatField('Price (ZAR)')
    item_Description = models.CharField(max_length=300)


    def __str__(self):
        return self.item_Type

    def save(self):
        super().save()

   