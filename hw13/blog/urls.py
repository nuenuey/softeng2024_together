from django.urls import path
from . import views

app_name = 'blog'  # 네임스페이스를 설정합니다.

urlpatterns = [
    path('tag/<str:slug>/', views.tag_page, name='tag_page'),
    path('category/<str:slug>/', views.category_page, name='category_page'),
    path('<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('', views.PostList.as_view(), name='post_list'),  # 여기에 이름 추가
]