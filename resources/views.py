from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Resource

def resource_list(request):
    resources = Resource.objects.all().order_by('category')
    return render(request, 'resources/resource_list.html', {'resources': resources})

def resource_detail(request, pk):
    resource = get_object_or_404(Resource, pk=pk)
    return render(request, 'resources/resource_detail.html', {'resource': resource})

