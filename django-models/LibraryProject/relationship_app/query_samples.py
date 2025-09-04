import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author_name = "George Orwell"
try:
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    print("Books by", author_name, ":", [book.title for book in books])
except Author.DoesNotExist:
    print("Author not found")

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
    librarian = Librarian.objects.get(library=library)
    print("Librarian of", library_name, ":", librarian.name)
except (Library.DoesNotExist, Librarian.DoesNotExist):
    print("No librarian found for", library_name)
