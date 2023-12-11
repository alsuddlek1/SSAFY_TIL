from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<pk>/', views.post, name='post'),
    path('<pk>/delete/', views.delete, name='delete'),
    path('<pk>/update/', views.update, name='update'),
]
