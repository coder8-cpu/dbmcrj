# Generated by Django 4.1.3 on 2023-02-12 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0036_alter_aqar_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='media/departments/img')),
            ],
        ),
        migrations.CreateModel(
            name='Eresources',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curiculam', models.FileField(null=True, upload_to='media/deparments/curiculam')),
                ('honours_resources', models.FileField(null=True, upload_to='media/departments/honours')),
                ('program_resources', models.FileField(null=True, upload_to='media/deparments/program')),
                ('departments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='public.departments')),
            ],
        ),
        migrations.CreateModel(
            name='DepartmentsFaculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('desgination', models.CharField(blank=True, max_length=50, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='media/pics/faculty')),
                ('specialization', models.CharField(blank=True, max_length=100, null=True)),
                ('qualification', models.CharField(blank=True, max_length=100, null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='public.departments')),
            ],
        ),
    ]
