from django.db import models

# Create your models here.
from django.db import models

class Author(models.Model):
    """
    Author model:
    Represents an author with a name field.
    One author can have multiple books (1-to-many relationship).
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model:
    Each book has a title, publication year, and is linked to an author.
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
