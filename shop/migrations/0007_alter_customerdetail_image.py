# Generated by Django 4.1.4 on 2022-12-21 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_alter_customerdetail_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerdetail',
            name='image',
            field=models.ImageField(default='', upload_to='shop/images'),
        ),
    ]
