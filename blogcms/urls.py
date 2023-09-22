from django.urls import path
from .views import PostDetail, PostList



urlpatterns = [
  path('posts/', PostList.as_view(), name="posts"),
  path('posts/<int:pk>', PostList.as_view(), name="post-details"),
  path('posts/<int:pk>',PostDetail.as_view(), name="post-details")
  
]