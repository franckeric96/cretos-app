# Generated by Django 3.0.8 on 2020-07-22 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialaccount',
            name='icon',
            field=models.CharField(choices=[('google-plus', 'fa-google-plus-g'), ('linkedin', 'fa-linkedin-in'), ('dribble', 'fa-dribbble'), ('facebook', 'fa-facebook'), ('rss', 'fa-rss'), ('instagram', 'fa-instagram'), ('pinterest', 'fa-pinterest'), ('flickr', 'fa-flickr')], max_length=20, null=True),
        ),
    ]
