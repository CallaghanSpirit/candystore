# Generated by Django 5.1.2 on 2024-11-24 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_goods_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='photo',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]