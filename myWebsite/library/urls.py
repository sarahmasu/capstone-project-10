from django.urls import path
from . import views

urlpatterns = [
    path('library', views.view_library, name='library'),
]