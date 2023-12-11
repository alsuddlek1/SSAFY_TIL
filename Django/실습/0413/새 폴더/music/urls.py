from django.urls import path
from . import views

app_name = 'music'
urlpatterns = [
    path('music/', views.music_list), # 모든 음악정보 조회
]
