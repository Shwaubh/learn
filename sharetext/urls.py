from django.urls import path
from . import views



urlpatterns = [
    path('', views.home),
    path('register/', views.register),
    path('login/', views.loginUser),
    path('logout/', views.logoutUser),
    path('sendmessage/', views.sendmessage),
    path('received/<int:user>', views.received),
    path('sent/<int:user>', views.sent)
]