from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'), # A에서 매칭되면 B로 처리해줘 
    path('<int:pk>/', views.detail, name='detail'),
]
