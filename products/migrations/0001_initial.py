# Generated by Django 5.0.7 on 2024-07-31 01:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('company', models.CharField(default='', max_length=20)),
                ('purpose', models.CharField(choices=[('의뢰 제작', '의뢰 제작'), ('중고 판매', '중고 판매'), ('중고 대여', '중고 대여')], default='', max_length=10)),
                ('category', models.CharField(choices=[('의상', '의상'), ('소품', '소품'), ('소모품', '소모품')], default='', max_length=10)),
                ('content', models.TextField(default='')),
                ('title', models.CharField(default='', max_length=50)),
                ('logo_img', models.ImageField(blank=True, null=True, upload_to='logo_images/')),
                ('price', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('company_num', models.CharField(default='', max_length=20)),
                ('company_img', models.ImageField(blank=True, null=True, upload_to='company_images/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('image_id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='post_images/')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='products.post')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('request_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=10)),
                ('number', models.CharField(default='', max_length=20)),
                ('address', models.CharField(default='', max_length=30)),
                ('content', models.TextField(default='')),
                ('reference_img', models.ImageField(blank=True, null=True, upload_to='reference_images/')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
