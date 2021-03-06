from django.urls import path
from .views import (
  PostDetailView,
  PrivatePostListView,
  PostListView,
  PostCreateView,
  PostUpdateView,
  PostDeleteView
)

urlpatterns = [
  path('', PostListView.as_view(), name='post_list'),
  path('new/', PostCreateView.as_view(), name='post_new'),
  path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
  path('<int:pk>/edit/', PostUpdateView.as_view(), name="post_edit"),
  path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
  path('private/', PrivatePostListView.as_view(), name='private_list'),
]