from django.contrib import admin
from .models import Post, PostImage, Request, ReferenceImage

admin.site.register(Post)
admin.site.register(PostImage)
admin.site.register(Request)
admin.site.register(ReferenceImage)