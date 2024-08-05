from django.db import models

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    purpose_choices = [
        ('의뢰 제작','의뢰 제작'),
        ('중고 판매','중고 판매'),
        ('중고 대여','중고 대여'),
    ]

    category_choices = [
        ('의상','의상'),
        ('소품','소품'),
        ('소모품','소모품'),
    ]

    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    company = models.CharField(max_length=20, default='', blank=True, null=True)
    purpose = models.CharField(max_length=10, choices=purpose_choices, default='')
    category = models.CharField(max_length=10, choices=category_choices, default='')
    address = models.CharField(max_length=40, default='', blank=True, null=True)
    rating = models.DecimalField(max_digits=5, decimal_places=1, default=0)
    title = models.CharField(max_length=50, default='', blank=True, null=True)
    content = models.TextField(default='', blank=True, null=True)
    content_img = models.FileField(upload_to='content_files/', blank=True, null=True)
    image1 = models.FileField(upload_to='content_files1/', blank=True, null=True, default='')
    image2 = models.FileField(upload_to='content_files2/', blank=True, null=True, default='')
    image3 = models.FileField(upload_to='content_files3/', blank=True, null=True, default='')
    image4 = models.FileField(upload_to='content_files4/', blank=True, null=True, default='')
    image5 = models.FileField(upload_to='content_files5/', blank=True, null=True, default='')
    promotion = models.TextField(default='', blank=True, null=True)
    logo_img = models.FileField(upload_to='logo_files/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    company_num = models.CharField(max_length=20, default='', blank=True, null=True)
    company_img = models.FileField(upload_to='company_files/', blank=True, null=True)

    def __str__(self):
        return f"{self.company}"

class Request(models.Model):
    request_id = models.AutoField(primary_key=True)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=10, default='')
    number = models.CharField(max_length=20, default='')
    address = models.CharField(max_length=30, default='')
    content = models.TextField(default='')
    reference = models.FileField(upload_to='reference_files/', blank=True, null=True)