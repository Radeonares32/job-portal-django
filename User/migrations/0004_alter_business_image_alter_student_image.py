# Generated by Django 4.0.1 on 2022-07-30 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_alter_business_image_alter_student_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='image',
            field=models.ImageField(upload_to='business/% Y/% m/% d/'),
        ),
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(null=True, upload_to='students/% Y/% m/% d/'),
        ),
    ]
