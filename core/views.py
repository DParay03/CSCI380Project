from django.shortcuts import render

from core.models import CrisisSupport


# Create your views here.
def root_page(request):
    return render(request, 'core/root.html')

def crisis_support(request):
    support = CrisisSupport.objects.all().order_by('category')
    return render(request, 'core/crisis_support.html', {'support': support})