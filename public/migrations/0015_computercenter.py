# Generated by Django 4.1.3 on 2023-01-16 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0014_academiccalander_courses_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComputerCenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/pics/computerlab')),
            ],
        ),
    ]
