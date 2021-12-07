from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('redirect-index/', views.redirect_index)
]
