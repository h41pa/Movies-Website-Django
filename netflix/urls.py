from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
    path('genre/<str:pk>/', views.genre, name='genre'),
    path('movie/<str:pk>/', views.movie, name='movie'),
    path('my_list/', views.my_list, name='my_list'),
    path('add_to_list/<uuid:movie_id>/', views.add_to_list, name='add_to_list'),
    path('search', views.search, name='search'),
]
