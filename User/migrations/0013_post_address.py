# Generated by Django 4.0.1 on 2022-07-31 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0012_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='address',
            field=models.CharField(max_length=100, null=True, verbose_name='address'),
        ),
    ]