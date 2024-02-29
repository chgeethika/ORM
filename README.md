# Ex02 Django ORM Web Application
## Date: 29/02/2024

## AIM
To develop a Django application to store and retrieve data from a Book database using Object Relational Mapping(ORM).

## Entity Relationship Diagram

![alt text](<Screenshot (254).png>)

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM

```
model.py

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
```
```
admin.py

from django.contrib import admin
from .models import Book,BookAdmin
admin.site.register(Book,BookAdmin)
```

## OUTPUT

![alt text](<Screenshot (255).png>)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
