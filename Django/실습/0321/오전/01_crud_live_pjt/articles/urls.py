from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    # 목록 조회
    path('', views.index, name='index'),
    # 개별 조회
    path('<int:pk>/', views.detail, name='detail'),
    # path('new/', views.new, name='new'),
    # 생성
    path('create/', views.create, name='create'),
    # 삭제
    path('<int:pk>/delete/', views.delete, name='delete'),
    # path('<int:pk>/edit/', views.edit, name='edit'),
    # 수정
    path('<int:pk>/update/', views.update, name='update'),
]
