import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author_name = "George Orwell"
books = Book.objects.filter(author__name=author_name)
print("Books by", author_name, ":", [book.title for book in books])

# List all books in a library
library_name = "Central Library"
try:
    library = Library.objects.get(name=library_name)
    books_in_library = library.books.all()
    print("Books in", library_name, ":", [book.title for book in books_in_library])
except Library.DoesNotExist:
    print("Library not found")

# Retrieve the librarian for a library
try:
    librarian = Librarian.objects.get(library__name=library_name)
    print("Librarian of", library_name, ":", librarian.name)
except Librarian.DoesNotExist:
    print("No librarian found for", library_name)
