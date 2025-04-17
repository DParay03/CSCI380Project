from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# Create your views here.


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'communityPost/communityPost.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'communityPost/communityPost.html'