# Generated by Django 4.1.3 on 2023-01-23 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0032_admissionquery_coursesfee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resource',
            old_name='dbm_lib_whatsapp_group_link3',
            new_name='label',
        ),
        migrations.RenameField(
            model_name='resource',
            old_name='dbm_whatsapp_group_link1',
            new_name='link',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='dbm_whatsapp_group_link2',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='internet_archive',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='ndli',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='online_public_access_catalog',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='wbclolr',
        ),
        migrations.AddField(
            model_name='resource',
            name='file',
            field=models.FileField(default=0, upload_to=''),
            preserve_default=False,
        ),
    ]
