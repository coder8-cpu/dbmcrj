# Generated by Django 4.1.3 on 2023-01-13 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0006_alter_facultymembers_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facultymembers',
            name='image',
            field=models.ImageField(upload_to='media/pics/faculty'),
        ),
    ]
