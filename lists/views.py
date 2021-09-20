from django.shortcuts import render
from .models import List

# Create your views here.
def index(request):
    lists = List.objects.all()
    context = {
        'lists' : lists
    }
    return render(request, 'lists/index.html', context)