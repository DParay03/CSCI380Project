from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, toggle_like, toggle_comment_like

urlpatterns = [
    path('', PostListView.as_view(), name='communityPost-home'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('new/', PostCreateView.as_view(), name='post-create'),
    path('<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('<int:pk>/like', toggle_like, name='toggle-like'),
    path('<int:pk>/comment/like', toggle_comment_like, name='toggle-comment-like'),
]