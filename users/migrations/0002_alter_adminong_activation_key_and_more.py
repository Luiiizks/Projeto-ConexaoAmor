# Generated by Django 4.2.6 on 2023-10-16 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminong',
            name='activation_key',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='adminong',
            name='password',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='adminong',
            name='username',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
