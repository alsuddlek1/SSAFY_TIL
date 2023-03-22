from django.urls import path
from . import views

# create, index, detail, update

urlpatterns = [
    path('index/', views.index, name="index"),
    path('create/', views.create, name="create"),
    
]
