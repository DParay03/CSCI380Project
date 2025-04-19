# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import JournalEntry
# Create your views here.

@login_required
def home(request):
    context = {
        'posts': JournalEntry.objects.all()
    }
    return render(request, 'journal/journal.html', context)


class JournalListView(ListView):
    model = JournalEntry
    template_name = 'journal/journal.html'
    context_object_name = 'journalEntry'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        return JournalEntry.objects.filter(user=self.request.user).order_by('-date_posted')

class JournalCreateView(LoginRequiredMixin, CreateView):
    model = JournalEntry
    fields = ['title', 'content']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('journal-list')  # Use the name of your journal list URL

class JournalUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = JournalEntry
    fields = ['title', 'content']
    success_url = '/journal'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False

class JournalDetailView(DetailView):
    model = JournalEntry
    template_name = 'journal/journal_detail.html'
    context_object_name = 'journalEntry'
    ordering = ['-date_posted']

class JournalDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = JournalEntry
    success_url = '/journal'
    template_name = 'journal/journal_confirm_delete.html'
    context_object_name = 'journalEntry'
    ordering = ['date_posted']

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False