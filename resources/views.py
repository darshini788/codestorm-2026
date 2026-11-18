from django.shortcuts import render
from .models import Resource

def resources_list_view(request):
    resources = Resource.objects.all().order_by('-uploaded_at')
    return render(request, 'resources/resources_list.html', {'resources': resources})
