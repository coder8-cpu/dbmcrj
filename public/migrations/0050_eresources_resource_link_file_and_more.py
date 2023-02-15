# Generated by Django 4.1.3 on 2023-02-15 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0049_indexalert_link_alter_indexalert_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='eresources',
            name='Resource_link_file',
            field=models.FileField(blank=True, null=True, upload_to='media/departments/resource/file/'),
        ),
        migrations.AlterField(
            model_name='administrativeofficer',
            name='desgination',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='administrativeofficer',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/pics/administrative'),
        ),
        migrations.AlterField(
            model_name='administrativeofficer',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='admissionnotice',
            name='carrer_counceling_date',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='admissionnotice',
            name='document_verification',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='admissionnotice',
            name='fees_payment',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='admissionnotice',
            name='hounours_course_date',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='admissionnotice',
            name='merit_publish_date',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='admissionnotice',
            name='program_course_date',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='admissionnotice',
            name='year',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='aqar',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='media/aqar/pdf'),
        ),
        migrations.AlterField(
            model_name='course_fee',
            name='course_fee',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='course_fee',
            name='course_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='departments',
            name='about',
            field=models.CharField(blank=True, max_length=100000000, null=True),
        ),
        migrations.AlterField(
            model_name='departments',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/departments/img'),
        ),
        migrations.AlterField(
            model_name='departments',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='departmentsfaculty',
            name='cv',
            field=models.FileField(blank=True, null=True, upload_to='media/deparments/cv'),
        ),
        migrations.AlterField(
            model_name='departmentsfaculty',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='documentrequired',
            name='label',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='eresources',
            name='Resource_link',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='eresources',
            name='honours_resources',
            field=models.FileField(blank=True, null=True, upload_to='media/departments/honours'),
        ),
        migrations.AlterField(
            model_name='eresources',
            name='honours_resources_label',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='eresources',
            name='program_resources',
            field=models.FileField(blank=True, null=True, upload_to='media/deparments/program'),
        ),
        migrations.AlterField(
            model_name='facultymembers',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='msg',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='governingbody',
            name='desgination',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='governingbody',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='indexalert',
            name='file',
            field=models.FileField(blank=True, max_length=1000000, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='indexalert',
            name='link',
            field=models.CharField(blank=True, max_length=1000000, null=True),
        ),
        migrations.AlterField(
            model_name='indexalert',
            name='message',
            field=models.CharField(blank=True, max_length=1000000, null=True),
        ),
        migrations.AlterField(
            model_name='iqac',
            name='desgination',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='iqac',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/pics/administrative'),
        ),
        migrations.AlterField(
            model_name='iqac',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='librarian',
            name='desgination',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='librarian',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/pics/lib'),
        ),
        migrations.AlterField(
            model_name='librarian',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='librarian',
            name='whatsapp',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='email',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='notice',
            name='notice_details',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='notice',
            name='notice_title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='notice_files',
            name='label',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='officestaff',
            name='desgination',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='officestaff',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
