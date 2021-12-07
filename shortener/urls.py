from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getuser/<int:member_id>/', views.get_user)
]
