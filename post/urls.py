from django.urls import path
from . import views


app_name = 'post'
urlpatterns = [
    path('add_post/', views.add_post, name='add_post'),
]
