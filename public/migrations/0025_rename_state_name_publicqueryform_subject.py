# Generated by Django 4.1.3 on 2023-01-22 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0024_remove_photogallary_img2_remove_photogallary_img3_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publicqueryform',
            old_name='state_name',
            new_name='subject',
        ),
    ]