from django.urls import path
from . import views

urlpatterns = [
   path('<int:pk>/', views.single_post, name='single_post'),
   path('', views.index, name='blog_index'),
]
