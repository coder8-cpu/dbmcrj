# Generated by Django 4.1.3 on 2023-01-16 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0017_alter_academiccalander_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndexAlert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=1000000)),
            ],
        ),
    ]