from django.urls import path
from .views import *

urlpatterns = [
    path('detail/<int:id>', detail, name = "detail"),
    path('new/', new, name="new"),
    path('edit/<int:id>', edit, name = "edit"),
    path('delete/<int:id>', delete, name ="delete"),
    path('search', search, name="search"),
]