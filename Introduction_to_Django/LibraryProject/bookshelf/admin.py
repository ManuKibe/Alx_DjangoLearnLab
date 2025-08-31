from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    # Show these fields in the admin list view
    list_display = ('title', 'author', 'publication_year')

    # Add filters on the sidebar
    list_filter = ('publication_year', 'author')

    # Enable search functionality
    search_fields = ('title', 'author')


# Register Book with custom admin configuration
admin.site.register(Book, BookAdmin)
