# Generated by Django 5.0.1 on 2024-01-21 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='status',
            field=models.CharField(default='Draft', max_length=30),
        ),
    ]
