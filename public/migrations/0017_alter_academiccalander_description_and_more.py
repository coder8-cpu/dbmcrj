# Generated by Django 4.1.3 on 2023-01-16 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0016_academiccalander_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academiccalander',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='academiccalander',
            name='link',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='administrativeofficer',
            name='desgination',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='administrativeofficer',
            name='image',
            field=models.ImageField(null=True, upload_to='media/pics/administrative'),
        ),
        migrations.AlterField(
            model_name='administrativeofficer',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='admissionnotice',
            name='carrer_counceling_date',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='admissionnotice',
            name='document_verification',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='admissionnotice',
            name='fees_payment',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='admissionnotice',
            name='hounours_course_date',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='admissionnotice',
            name='merit_publish_date',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='admissionnotice',
            name='program_course_date',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='admissionnotice',
            name='year',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='books_in_digit',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='department_name',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='canteen',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/pics/canteen'),
        ),
        migrations.AlterField(
            model_name='carrerguidence',
            name='link',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='carrerguidence',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='computercenter',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/pics/computerlab'),
        ),
        migrations.AlterField(
            model_name='course_fee',
            name='course_fee',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='course_fee',
            name='course_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='courses',
            name='coursename',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='courses',
            name='courseseats',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='courses',
            name='year',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='facultymembers',
            name='department',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='facultymembers',
            name='desgination',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='facultymembers',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='media/pics/faculty'),
        ),
        migrations.AlterField(
            model_name='facultymembers',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='facultymembers',
            name='qualification',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='facultymembers',
            name='specialization',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='governingbody',
            name='desgination',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='governingbody',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='librarian',
            name='desgination',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='librarian',
            name='image',
            field=models.ImageField(null=True, upload_to='media/pics/lib'),
        ),
        migrations.AlterField(
            model_name='librarian',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='librarian',
            name='whatsapp',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='mamangementmembers',
            name='name',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='mamangementmembers',
            name='slno',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='officestaff',
            name='desgination',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='officestaff',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='photogallary',
            name='img1',
            field=models.ImageField(blank=True, null=True, upload_to='media/pics/gallary'),
        ),
        migrations.AlterField(
            model_name='photogallary',
            name='img2',
            field=models.ImageField(blank=True, null=True, upload_to='media/pics/gallary'),
        ),
        migrations.AlterField(
            model_name='photogallary',
            name='img3',
            field=models.ImageField(blank=True, null=True, upload_to='media/pics/gallary'),
        ),
        migrations.AlterField(
            model_name='photogallary',
            name='img4',
            field=models.ImageField(blank=True, null=True, upload_to='media/pics/gallary'),
        ),
        migrations.AlterField(
            model_name='photogallary',
            name='img5',
            field=models.ImageField(blank=True, null=True, upload_to='media/pics/gallary'),
        ),
        migrations.AlterField(
            model_name='photogallary',
            name='img6',
            field=models.ImageField(blank=True, null=True, upload_to='media/pics/gallary'),
        ),
        migrations.AlterField(
            model_name='photogallary',
            name='img7',
            field=models.ImageField(blank=True, null=True, upload_to='media/pics/gallary'),
        ),
        migrations.AlterField(
            model_name='photogallary',
            name='img8',
            field=models.ImageField(blank=True, null=True, upload_to='media/pics/gallary'),
        ),
        migrations.AlterField(
            model_name='principleimage',
            name='img1',
            field=models.ImageField(blank=True, null=True, upload_to='media/pics/principle'),
        ),
        migrations.AlterField(
            model_name='principleimage',
            name='principle_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='publicqueryform',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='publicqueryform',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='publicqueryform',
            name='query',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='publicqueryform',
            name='state_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='referencebooks',
            name='Reference_catagory',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='referencebooks',
            name='books_available',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='dbm_lib_whatsapp_group_link3',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='dbm_whatsapp_group_link1',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='dbm_whatsapp_group_link2',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='internet_archive',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='ndli',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='online_public_access_catalog',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='wbclolr',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='sliderimage',
            name='img1',
            field=models.ImageField(blank=True, null=True, upload_to='media/pics/slider'),
        ),
        migrations.AlterField(
            model_name='sliderimage',
            name='img2',
            field=models.ImageField(blank=True, null=True, upload_to='media/pics/slider'),
        ),
        migrations.AlterField(
            model_name='sliderimage',
            name='img3',
            field=models.ImageField(blank=True, null=True, upload_to='media/pics/slider'),
        ),
        migrations.AlterField(
            model_name='sliderimage',
            name='img4',
            field=models.ImageField(blank=True, null=True, upload_to='media/pics/slider'),
        ),
        migrations.AlterField(
            model_name='sliderimage',
            name='img5',
            field=models.ImageField(blank=True, null=True, upload_to='media/pics/slider'),
        ),
        migrations.AlterField(
            model_name='teacherscouncil',
            name='desgination',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='teacherscouncil',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='teacherscouncil',
            name='qualification',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
