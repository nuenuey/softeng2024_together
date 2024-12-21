from django.urls import path
from . import views
from .views import PostList, PostDetail, reserve

app_name = "home"



urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('reserve/<int:pk>/', views.reserve, name='reserve'),
    path('reserve/process/', views.reserve_process, name='reserve_process'),
]