# Generated by Django 4.1.3 on 2023-01-13 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0008_rename_image_facultymembers_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='librarian',
            name='desgination',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='librarian',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='librarian',
            name='whatsapp',
            field=models.CharField(max_length=10),
        ),
    ]