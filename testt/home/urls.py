from django.urls import path
from . import views
from .views import PostList, PostDetail, reserve
app_name = "home"

urlpatterns = [
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('reserve/', views.reserve, name='reserve'),
    path('reserve/process/', views.reserve_process, name='reserve_process'),
]