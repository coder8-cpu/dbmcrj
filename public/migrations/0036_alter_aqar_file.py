# Generated by Django 4.1.3 on 2023-02-12 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0035_aqar_iqac'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aqar',
            name='file',
            field=models.FileField(null=True, upload_to='media/aqar/pdf'),
        ),
    ]
