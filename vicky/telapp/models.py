from django.db import models
from django.contrib import admin
class Book(models.Model):
    id=models.IntegerField(primary_key=True);
    author=models.CharField(max_length=20);
    name=models.CharField(max_length=50);
    yearofpublish=models.DateField();
    price=models.IntegerField();
class BookAdmin(admin.ModelAdmin):
    list_display=("id","author","name","yearofpublish","price");
