# Generated by Django 5.0.7 on 2024-07-27 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productionpost',
            name='category',
            field=models.CharField(default='미분류', max_length=50),
        ),
        migrations.AddField(
            model_name='productionpost',
            name='company',
            field=models.CharField(default='미기입', max_length=20),
        ),
        migrations.AddField(
            model_name='productionpost',
            name='company_img',
            field=models.ImageField(blank=True, null=True, upload_to='company_images/'),
        ),
        migrations.AddField(
            model_name='productionpost',
            name='company_num',
            field=models.CharField(default='0', max_length=20),
        ),
        migrations.AddField(
            model_name='productionpost',
            name='content',
            field=models.TextField(default='미기입'),
        ),
        migrations.AddField(
            model_name='productionpost',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='production_images/'),
        ),
        migrations.AddField(
            model_name='productionpost',
            name='logo_img',
            field=models.ImageField(blank=True, null=True, upload_to='logo_images/'),
        ),
        migrations.AddField(
            model_name='productionpost',
            name='price',
            field=models.DecimalField(decimal_places=2, default='0', max_digits=10),
        ),
        migrations.AddField(
            model_name='productionpost',
            name='title',
            field=models.CharField(default='미기입', max_length=100),
        ),
    ]
