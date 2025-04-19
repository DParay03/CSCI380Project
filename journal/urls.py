from django.urls import path
from .views import JournalListView, JournalDetailView, JournalCreateView, JournalUpdateView, JournalDeleteView

urlpatterns = [
    path('', JournalListView.as_view(), name='journal-home'),
    path('<int:pk>/', JournalDetailView.as_view(), name='journal-detail'),
    path('new/', JournalCreateView.as_view(), name='journal-create'),
    path('<int:pk>/update/', JournalUpdateView.as_view(), name='journal-update'),
    path('<int:pk>/delete/', JournalDeleteView.as_view(), name='journal-delete'),
]