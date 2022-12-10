from django.contrib import admin
from .models import Company, Review, Service, Product, Document

# Register your models here.

admin.site.register(Company)
admin.site.register(Review)
admin.site.register(Service)
admin.site.register(Product)
admin.site.register(Document)

