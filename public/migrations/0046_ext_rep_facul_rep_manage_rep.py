# Generated by Django 4.1.3 on 2023-02-13 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0045_rename_description_academiccalander_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ext_rep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('desgination', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Facul_rep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('desgination', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Manage_rep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('desgination', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
