# Generated by Django 2.2.13 on 2021-07-11 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiledetail',
            name='email',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='profiledetail',
            name='number',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
    ]
