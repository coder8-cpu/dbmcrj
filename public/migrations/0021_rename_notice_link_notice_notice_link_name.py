# Generated by Django 4.1.3 on 2023-01-22 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0020_notice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notice',
            old_name='notice_link',
            new_name='notice_link_name',
        ),
    ]
