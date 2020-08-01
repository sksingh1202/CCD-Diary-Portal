from django.db import models
from django.contrib import auth
from datetime import datetime
from django.utils.text import slugify

# Create your models here.

class User(auth.models.User, auth.models.PermissionsMixin):
    def __str__(self):
        return self.username

class Company(models.Model):
    CompanyName = models.CharField(max_length=100)
    POC         = models.CharField(max_length=100, blank=True, default = '')
    CPOC        = models.CharField(max_length=100, blank=True, default = '')
    order       = models.AutoField(primary_key=True)
    TopRemark   = models.TextField()
    placement   = models.BooleanField()
    # slug = models.SlugField(allow_unicode=True, unique=True, blank=True)

    def __str__(self):
        return self.CompanyName

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.CompanyName)
    #     super().save(*args, **kwargs)

class Remarks(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE,default=0,related_name='remarks')
    POC = models.CharField(max_length=100, default = "None")
    CPOC = models.CharField(max_length=100, default = "None")
    remark = models.TextField()
    datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company.CompanyName
