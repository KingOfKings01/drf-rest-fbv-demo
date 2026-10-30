from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/book/', views.book_view),
    path('api/book/<int:pk>/', views.book_detail_view),
]