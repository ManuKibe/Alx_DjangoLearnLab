from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    """
    A form for the Book model to demonstrate secure input handling.
    """
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']
        "ExampleForm"
