# Generated by Django 2.2.6 on 2019-11-05 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qr', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='qr',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
