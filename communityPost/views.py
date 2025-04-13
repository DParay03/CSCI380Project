from django.shortcuts import render

# Create your views here.

posts = [
    {
        'author': '<NAME>',
        'title': '<NAME>',
        'text': '<NAMEsa,mdkfbhkajsdhfljksaljkfdsahkjfhdslajkhfjdksahkf>',
        'date': '05/10/03'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'communityPost.html', context)