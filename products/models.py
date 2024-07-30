from django.db import models

class Post(models.Model):
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
    company = models.CharField(max_length=20, default='')
    purpose = models.CharField(max_length=10, choices=purpose_choices, default='')
    category = models.CharField(max_length=10, choices=category_choices, default='')
    content = models.TextField(default='')
    title = models.CharField(max_length=50, default='')
    logo_img = models.ImageField(upload_to='logo_images/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    company_num = models.CharField(max_length=20, default='')
    company_img = models.ImageField(upload_to='company_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.company}"

class PostImage(models.Model):
    post = models.ForeignKey(Post, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images/')

    def __str__(self):
        return f"{self.post}"

class Request(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=10, default='')
    number = models.CharField(max_length=20, default='')
    address = models.CharField(max_length=30, default='')
    content = models.TextField(default='')
    reference_img = models.ImageField(upload_to='reference_images/', blank=True, null=True)