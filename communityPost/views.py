from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Comment
from .forms import CommentForm

# Create your views here.

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'communityPost/communityPost.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'communityPost/communityPost.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

# List all posts by a specific user
class UserPostListView(ListView):
    model = Post
    template_name = 'communityPost/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

# Create a new post, user must be logged in with 'LoginRequiredMixin' parameter
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user == self.get_object().author

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    fields = ['content']
    context_object_name = 'comment'

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.post.pk})

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user == self.get_object().author

class PostDetailView(DetailView):
    model = Post
    template_name = 'communityPost/communityPost_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['comments'] = self.object.comment_set.all()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.author = request.user
            parent_id = request.POST.get('parent_id')
            if parent_id:
                comment.parent_id = parent_id
            comment.save()
        return redirect('post-detail', pk=self.object.pk)

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'communityPost/post_confirm_delete.html'
    success_url = '/communityPost'
    context_object_name = 'post'

    def test_func(self):
        return self.request.user == self.get_object().author

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'communityPost/comment_confirm_delete.html'
    context_object_name = 'comment'

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.post.pk})

    def test_func(self):
        return self.request.user == self.get_object().author

# Toggle like/unlike for a post and send email notification on like
def toggle_like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
        send_mail(
            subject='Someone liked your post!',
            message=f'{request.user.username} liked your post: "{post.title}".',
            from_email=None,  # uses DEFAULT_FROM_EMAIL from settings
            recipient_list=[post.author.email],
            fail_silently=True,
        )
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# Toggle like/unlike for a comment
def toggle_comment_like(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post = comment.post
    if request.user in comment.likes.all():
        comment.likes.remove(request.user)
    else:
        comment.likes.add(request.user)
        send_mail(
        subject='Someone liked your Comment!',
        message=f'{request.user.username} liked your comment: "{comment.content}" on Post: "{post.title}".',
        from_email=None,  # uses DEFAULT_FROM_EMAIL from settings
        recipient_list=[request.user.email],
        fail_silently=True, # False for debugging
    )
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))