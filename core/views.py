from django.shortcuts import render

# Create your views here.
def root_page(request):
    return render(request, 'core/root.html')
