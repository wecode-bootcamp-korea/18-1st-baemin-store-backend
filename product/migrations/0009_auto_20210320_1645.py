# Generated by Django 3.1.7 on 2021-03-20 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_product_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinquiry',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='1994-11-15'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productinquiry',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='review',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='1995-11-15'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
