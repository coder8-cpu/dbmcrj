# Generated by Django 4.1.3 on 2023-01-22 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0025_rename_state_name_publicqueryform_subject'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publicqueryform',
            old_name='first_name',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='publicqueryform',
            old_name='last_name',
            new_name='name',
        ),
    ]