# Ex02 Django ORM Web Application
## Date: 29/02/2024

## AIM
To develop a Django application to store and retrieve data from a Book database using Object Relational Mapping(ORM).

## Entity Relationship Diagram

![Screenshot (312)](https://github.com/chgeethika/ORM/assets/142209368/ad845538-a65c-4c18-82c5-e968e1df8d94)


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
models.py

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


![Screenshot (313)](https://github.com/chgeethika/ORM/assets/142209368/f4956958-86d1-4f03-982d-da07bdfe8abf)



## RESULT
Thus the program for creating a database using ORM hass been executed successfully
