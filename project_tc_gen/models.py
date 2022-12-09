from django.db import models
from email.policy import default
from django.db import models
from datetime import datetime
import uuid
from django.contrib.auth.models import User
from users.models import Profile

# Create your models here.

class Company(models.Model):
    company_name = models.CharField(max_length=100)
    company_website_url = models.CharField(max_length=100)
    app_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    company_email = models.CharField(max_length=100)
    company_address = models.CharField(max_length=100)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.company_name


class Review(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.PROTECT)
    review_id = models.IntegerField()
    reviews = models.TextField(null=False, blank=False)
    rating = models.IntegerField()


    def __str__(self):
        return self.reviews

class Service(models.Model):
    service_id = models.IntegerField()
    name = models.CharField(max_length=100)
    description = models.TextField(null=False, blank=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Product(models.Model):
    product_id = models.IntegerField()
    name = models.CharField(max_length=100)
    description = models.TextField(null=False, blank=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Document(models.Model):
    document_id = models.IntegerField()
    document_type = models.CharField(max_length=100)
    document_content = models.TextField(null=False, blank=False)
    effective_date = models.DateTimeField(auto_now_add=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.document_type

