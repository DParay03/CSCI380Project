from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    CommentUpdateView,
    CommentDeleteView,
    toggle_like,
    toggle_comment_like,
)

urlpatterns = [
    path('', PostListView.as_view(), name='communityPost-home'),

    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),

    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),

    path('new/', PostCreateView.as_view(), name='post-create'),

    path('<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),

    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    # Toggle like on a post
    path('<int:pk>/like', toggle_like, name='toggle-like'),

    # Toggle like on a comment
    path('<int:pk>/comment/like', toggle_comment_like, name='toggle-comment-like'),

    path('<int:pk>/comment/update', CommentUpdateView.as_view(), name='comment-update'),

    path('<int:pk>/comment/delete', CommentDeleteView.as_view(), name='comment-delete'),
]