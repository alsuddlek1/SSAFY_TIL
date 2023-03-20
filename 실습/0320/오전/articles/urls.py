from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/',views.detail, name='detail'),
    path('new/', views.new,name='new'),
    path('create/', views.create, name='create'),
    path('edit/<int:article_pk>', views.edit, name='edit'),
    path('update/<int:article_pk>', views.update, name='update'),
    path('delete/<int:article_pk>', views.delete, name='delete')
]
