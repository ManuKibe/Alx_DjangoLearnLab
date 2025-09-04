from django.urls import path
from . import views

urlpatterns = [
    path("books/", views.list_books, name="list_books"),
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),
]
from django.contrib import admin
from django.urls import path, include
from .views import list_books
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('relationship_app.urls')),
]
from django.urls import path
from .views import list_books, LibraryDetailView, register, CustomLoginView, CustomLogoutView

urlpatterns = [
    # Books & Library views
    path("books/", list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),

    # Authentication views
    path("register/", register, name="register"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
]
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views   # ✅ so "views.register" appears

urlpatterns = [
    # Books & Libraries
    path("books/", views.list_books, name="list_books"),
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),


    # Authentication
    path("register/", views.register, name="register"),
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
]
from django.urls import path
from . import views

urlpatterns = [
    path("admin-view/", views.admin_view, name="admin_view"),
    path("librarian-view/", views.librarian_view, name="librarian_view"),
    path("member-view/", views.member_view, name="member_view"),
]
from django.urls import path
from . import views

urlpatterns = [
    path("books/add/", views.add_book, name="add_book"),
    path("books/<int:pk>/edit/", views.edit_book, name="edit_book"),
    path("books/<int:pk>/delete/", views.delete_book, name="delete_book"),
]
