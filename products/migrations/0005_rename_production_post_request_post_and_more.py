# Generated by Django 5.0.7 on 2024-07-30 05:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_remove_rentalpost_user_remove_salespost_user_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='request',
            old_name='production_post',
            new_name='post',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='purpose',
            field=models.CharField(choices=[('의뢰 제작', '의뢰 제작'), ('중고 판매', '중고 판매'), ('중고 대여', '중고 대여')], default='', max_length=10),
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='post_images/')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.post')),
            ],
        ),
    ]
