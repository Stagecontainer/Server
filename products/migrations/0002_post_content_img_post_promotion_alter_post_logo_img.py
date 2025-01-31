# Generated by Django 5.0.7 on 2024-08-02 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content_img',
            field=models.FileField(blank=True, null=True, upload_to='content_files/'),
        ),
        migrations.AddField(
            model_name='post',
            name='promotion',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='logo_img',
            field=models.FileField(blank=True, null=True, upload_to='logo_files/'),
        ),
    ]
