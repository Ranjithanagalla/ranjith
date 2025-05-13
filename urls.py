from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),      # Page 1
    path('title/', views.title_view, name='title') # Page 2
]
