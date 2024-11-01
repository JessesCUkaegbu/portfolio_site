# Generated by Django 5.1.2 on 2024-11-01 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=30)),
                ('img', models.ImageField(upload_to='portfolio')),
                ('video', models.FileField(upload_to='')),
                ('detail', models.TextField()),
            ],
        ),
    ]
