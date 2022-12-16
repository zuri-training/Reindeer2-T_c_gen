from django.contrib import admin
from .models import Company, Review, Service, Product, Document



class CompanyAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Company Details", {"fields": ['company_name', 'company_address', 'company_email','country']}),
        ("Website/APP Details", {"fields": ['app_name', 'company_website_url']}),
        ("Date", {"fields": ['policy_date']})
       
    ]


# Register your models here.

admin.site.register(Company, CompanyAdmin)
admin.site.register(Review)
admin.site.register(Service)
admin.site.register(Product)
admin.site.register(Document)


