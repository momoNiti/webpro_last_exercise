
from . import views
from django.urls import path

urlpatterns = [
    path('index/', views.index, name="index"),
    path('login/', views.my_login, name='login'),
    path('request/', views.request_form, name='request-form'),
    path('logout/', views.my_logout, name='logout')
]