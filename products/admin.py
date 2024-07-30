from django.contrib import admin
from .models import Post, PostImage, Request

admin.site.register(Post)
admin.site.register(PostImage)
admin.site.register(Request)