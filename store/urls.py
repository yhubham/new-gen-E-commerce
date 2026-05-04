# store/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # This maps the empty path '' to the home view function
    path('', views.home, name='home'),
]