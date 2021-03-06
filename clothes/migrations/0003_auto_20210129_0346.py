# Generated by Django 3.1.4 on 2021-01-29 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0002_item_item_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='item_description',
            new_name='item_Description',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='item_name',
            new_name='item_Name',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='item_price',
            new_name='item_Price',
        ),
        migrations.RemoveField(
            model_name='item',
            name='item_image',
        ),
        migrations.RemoveField(
            model_name='item',
            name='item_type',
        ),
        migrations.AddField(
            model_name='item',
            name='item_Image',
            field=models.ImageField(default='images', upload_to='clothes/static/img/<django.db.models.fields.CharField>/images'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='item_Type',
            field=models.CharField(choices=[('caps', 'Caps'), ('coats', 'Coats'), ('hats', 'Hats'), ('hoodies', 'Hoodies'), ('jackets', 'Jackets'), ('jackets', 'Jackets'), ('shirts', 'Shirts'), ('skits', 'Skirts'), ('sweaters', 'Sweaters'), ('waistcoats', 'Waistcoats')], default='caps', max_length=30),
        ),
    ]
