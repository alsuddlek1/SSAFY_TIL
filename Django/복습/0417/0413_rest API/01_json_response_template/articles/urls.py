from django.urls import path
from . import views


urlpatterns = [
    # path('html/', views.article_html),
    # path('json-1/', views.article_json_1),
    # path('json-2/', views.article_json_2),
    # path('json-3/', views.article_json_3),
    path('articles/', views.article_list),
    path('articles/<int:article_pk>', views.article_detail),
    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
    path('articles/<int:article_pk>/comments/', views.comment_create),
]
