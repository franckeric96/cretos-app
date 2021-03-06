# Generated by Django 3.0.8 on 2020-07-23 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='nom',
        ),
        migrations.AddField(
            model_name='product',
            name='date_add',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='date_update',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='products/'),
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.BooleanField(default=True, null=True),
        ),
    ]
