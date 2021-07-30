from django.urls import path
from .views import *

urlpatterns = [
    path('detail/<int:post_id>', detail, name = "detail"),
    path('new/', new, name="new"),
    path('edit/<int:id>', edit, name = "edit"),
    path('delete/<int:id>', delete, name ="delete"),
    path('search', search, name="search"),
    path('detail/<int:post_id>/comment', create_comment, name="comment"),
    path('detail/<int:post_id>/comment/<int:comment_id>', create_re_comment, name="re_comment"),
]