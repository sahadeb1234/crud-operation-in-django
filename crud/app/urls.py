from django.urls import path
from app import views

urlpatterns = [
path('',  views.index, name="index"),
path('delete/<int:id>/', views.delete, name="deletedata"),
path('<int:id>/', views.update, name="update")
     
]