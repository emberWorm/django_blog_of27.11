from django.urls import path
from .views import *
urlpatterns = [
    path('', home),
    path('new_temp/', new_temp, name='new_temp'),
]
