from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='index'),
    path('new_post', views.PostCreateView.as_view(), name='new_post'),
]