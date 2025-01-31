# Generated by Django 5.0.7 on 2024-08-05 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_post_rating_alter_post_promotion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image1',
            field=models.FileField(blank=True, default='', null=True, upload_to='content_files1/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image2',
            field=models.FileField(blank=True, default='', null=True, upload_to='content_files2/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image3',
            field=models.FileField(blank=True, default='', null=True, upload_to='content_files3/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image4',
            field=models.FileField(blank=True, default='', null=True, upload_to='content_files4/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image5',
            field=models.FileField(blank=True, default='', null=True, upload_to='content_files5/'),
        ),
    ]
