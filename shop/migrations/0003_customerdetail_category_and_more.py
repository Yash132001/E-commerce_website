# Generated by Django 4.1.4 on 2022-12-21 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_customerdetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerdetail',
            name='category',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='customerdetail',
            name='customer_email',
            field=models.EmailField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='customerdetail',
            name='image',
            field=models.ImageField(default='', upload_to='shop/images'),
        ),
        migrations.AddField(
            model_name='customerdetail',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customerdetail',
            name='subcategory',
            field=models.CharField(default='', max_length=50),
        ),
    ]
