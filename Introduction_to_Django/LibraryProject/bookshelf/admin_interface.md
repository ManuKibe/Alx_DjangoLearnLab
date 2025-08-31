# Utilizing the Django Admin Interface

## Objective
Gain practical experience with the Django admin interface by configuring the admin to manage the Book model.

## Steps

### 1. Register the Book Model
In `bookshelf/admin.py`, import and register the `Book` model:

```python
from django.contrib import admin
from .models import Book
