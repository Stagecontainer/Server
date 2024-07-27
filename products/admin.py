from django.contrib import admin
from .models import ProductionPost, SalesPost, RentalPost, RequestPost

admin.site.register(ProductionPost)
admin.site.register(SalesPost)
admin.site.register(RentalPost)
admin.site.register(RequestPost)