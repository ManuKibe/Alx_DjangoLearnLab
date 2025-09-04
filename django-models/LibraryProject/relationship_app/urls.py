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
