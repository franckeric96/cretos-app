# Generated by Django 3.0.8 on 2020-07-25 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_auto_20200725_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialaccount',
            name='icon',
            field=models.CharField(choices=[('pinterest', 'fa-pinterest'), ('rss', 'fa-rss'), ('dribble', 'fa-dribbble'), ('linkedin', 'fa-linkedin-in'), ('facebook', 'fa-facebook'), ('google-plus', 'fa-google-plus-g'), ('flickr', 'fa-flickr'), ('instagram', 'fa-instagram')], max_length=20, null=True),
        ),
    ]
