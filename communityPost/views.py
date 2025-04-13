from django.shortcuts import render
from .models import Post

# Create your views here.

posts = [
    {
        'author': '<NAME>',
        'title': '<Nsfsfsd>',
        'content': 'NAMEsa,mdkfbhkajsdhfljksaljkfdsahkjfhdslajkhfjdksahkf',
        'date_posted': '05/10/03'
    }
]

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'communityPost/communityPost.html', context)