# Generated by Django 3.2.8 on 2021-11-03 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0012_remove_ingredient_recipe'),
    ]

    operations = [
        migrations.CreateModel(
            name='LookupIngRecQty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to='recipes.ingredient')),
                ('quantity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quantities', to='recipes.quantity')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='recipes.recipe')),
            ],
        ),
        migrations.RemoveField(
            model_name='lookupingrec',
            name='ingredient',
        ),
        migrations.RemoveField(
            model_name='lookupingrec',
            name='recipe',
        ),
        migrations.DeleteModel(
            name='LookupIngQty',
        ),
        migrations.DeleteModel(
            name='LookupIngRec',
        ),
    ]