# Generated by Django 4.1.3 on 2023-02-13 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0046_ext_rep_facul_rep_manage_rep'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ext_rep',
            name='desgination',
            field=models.CharField(max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='ext_rep',
            name='name',
            field=models.CharField(max_length=3000, null=True),
        ),
        migrations.AlterField(
            model_name='facul_rep',
            name='desgination',
            field=models.CharField(max_length=50009, null=True),
        ),
        migrations.AlterField(
            model_name='facul_rep',
            name='name',
            field=models.CharField(max_length=30000, null=True),
        ),
    ]
