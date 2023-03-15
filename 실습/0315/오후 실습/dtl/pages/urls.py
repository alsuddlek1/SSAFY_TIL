from django.urls import path
from . import views

# 변수명 app_name 은 꼭 지켜야 함
app_name = 'pages'

urlpatterns = [
    # URL mapping -> include
    # Naming URL patterns
    path('index/', views.index, name='index'),
    # path('주소창에 쓰는 내용/', import받아온 모듈의 함수명, name='이 경로를 부를 이름')
    path('create/', views.create, name='create'),
    
]