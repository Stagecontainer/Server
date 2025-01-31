# Generated by Django 5.0.7 on 2024-08-02 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_post_company_alter_post_content_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='referenceimage',
            name='request',
        ),
        migrations.AddField(
            model_name='post',
            name='address',
            field=models.CharField(blank=True, default='', max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='image1',
            field=models.FileField(blank=True, null=True, upload_to='content_files/'),
        ),
        migrations.AddField(
            model_name='post',
            name='image2',
            field=models.FileField(blank=True, null=True, upload_to='content_files/'),
        ),
        migrations.AddField(
            model_name='post',
            name='image3',
            field=models.FileField(blank=True, null=True, upload_to='content_files/'),
        ),
        migrations.AddField(
            model_name='post',
            name='image4',
            field=models.FileField(blank=True, null=True, upload_to='content_files/'),
        ),
        migrations.AddField(
            model_name='post',
            name='image5',
            field=models.FileField(blank=True, null=True, upload_to='content_files/'),
        ),
        migrations.AddField(
            model_name='request',
            name='reference',
            field=models.FileField(blank=True, null=True, upload_to='reference_files/'),
        ),
        migrations.DeleteModel(
            name='PostImage',
        ),
        migrations.DeleteModel(
            name='ReferenceImage',
        ),
    ]
