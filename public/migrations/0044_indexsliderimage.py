# Generated by Django 4.1.3 on 2023-02-13 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0043_remove_eresources_curiculam_departmentsfaculty_cv_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndexSliderImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img1', models.ImageField(blank=True, null=True, upload_to='media/pics/slider')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]
