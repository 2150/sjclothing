from django.db import models

class Item(models.Model):
    ITEM_CHOICES = (('caps', 'Caps'), ('coats', 'Coats'), ('hats', 'Hats'), ('hoodies', 'Hoodies'), ('jackets', 'Jackets'), 
                    ('jackets', 'Jackets'), ('shirts', 'Shirts'), ('skits', 'Skirts'), ('sweaters', 'Sweaters'), 
                    ('waistcoats', 'Waistcoats'))

    item_Type = models.CharField(max_length=30, choices=ITEM_CHOICES, default='caps')
    item_Name = models.CharField(max_length=100)
    
    item_Image = models.ImageField(upload_to='static/img/' + str(item_Type))
    item_Price = models.FloatField('Price')
    item_Description = models.CharField(max_length=300)