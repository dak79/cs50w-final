# Generated by Django 3.2.8 on 2021-11-03 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_ingredient_preparation_recipe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='recipe',
        ),
        migrations.AddField(
            model_name='ingredient',
            name='recipe',
            field=models.ManyToManyField(related_name='ingredient', to='recipes.Recipe'),
        ),
    ]
