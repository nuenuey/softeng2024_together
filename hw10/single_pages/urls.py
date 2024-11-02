from django.urls import path
from . import views

app_name = 'single_pages'

urlpatterns = [
    path('about_me/',views.about_me),
    path('', views.landing_page, name='index'),
    path('dodo/', views.dodo_page, name='dodo'),
    path('flower/', views.flower_page, name='flower'),
    path('king/', views.king_page, name='king'),
    path('onedanggo/', views.onedanggo_page, name='onedanggo'),
    path('posts/', views.posts_page, name='posts'),
    path('soba/', views.soba_page, name='soba'),
    path('soonday/', views.soonday_page, name='soonday'),
]