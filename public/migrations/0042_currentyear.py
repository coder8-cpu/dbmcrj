# Generated by Django 4.1.3 on 2023-02-13 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0041_resource_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='currentyear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]
