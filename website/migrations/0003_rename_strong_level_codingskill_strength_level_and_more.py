# Generated by Django 5.1.2 on 2024-11-01 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_portfolio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='codingskill',
            old_name='strong_level',
            new_name='strength_level',
        ),
        migrations.RenameField(
            model_name='designskill',
            old_name='strong_level',
            new_name='strength_level',
        ),
    ]