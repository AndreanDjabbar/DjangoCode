# Generated by Django 5.0.1 on 2024-02-05 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LoginForm',
        ),
        migrations.DeleteModel(
            name='LoginModel',
        ),
    ]
