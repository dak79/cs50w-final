# Generated by Django 3.2.8 on 2021-11-03 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_auto_20211103_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='imageURL',
            field=models.URLField(blank=True, null=True),
        ),
    ]
