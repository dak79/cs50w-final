# Generated by Django 3.2.8 on 2021-11-03 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0011_lookupingrec'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='recipe',
        ),
    ]
