from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),   
    path("saveText", views.saveText, name="saveText"),  
    path('post/<int:id>', views.post, name="post")
]