# Generated by Django 4.1.3 on 2023-01-23 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myfamily', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daughter',
            name='brother',
            field=models.ManyToManyField(blank=True, to='myfamily.son'),
        ),
        migrations.AlterField(
            model_name='son',
            name='grandfather',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='grandson', to='myfamily.grandfather'),
        ),
        migrations.AlterField(
            model_name='son',
            name='sister',
            field=models.ManyToManyField(to='myfamily.daughter'),
        ),
    ]
