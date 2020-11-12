from django.urls import path
from Restaurant_Search import views


urlpatterns = [
    path('',views.home, name="home"),
    path('searchRestaurant',views.searchRestaurant, name="searchRestaurant"),
]
