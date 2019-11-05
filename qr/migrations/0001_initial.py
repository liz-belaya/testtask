# Generated by Django 2.2.6 on 2019-10-30 14:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Qr',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('campaign', models.CharField(max_length=200)),
                ('sourse', models.CharField(max_length=200)),
                ('product', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('number_of_transitions', models.IntegerField(default=0)),

            ],
        ),
    ]
