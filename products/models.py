from django.db import models

class ProductionPost(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    company = models.CharField(max_length=20, default='미기입')
    category = models.CharField(max_length=50, default='미분류')
    content = models.TextField(default='미기입')
    image = models.ImageField(upload_to='production_images/', blank=True, null=True)
    title = models.CharField(max_length=100, default='미기입')
    logo_img = models.ImageField(upload_to='logo_images/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default='0')
    company_num = models.CharField(max_length=20, default='0')
    company_img = models.ImageField(upload_to='company_images/', blank=True, null=True)

class SalesPost(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)

class RentalPost(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)

class RequestPost(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    production_post = models.ForeignKey(ProductionPost, on_delete=models.CASCADE)