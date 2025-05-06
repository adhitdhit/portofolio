
# Create your views here.
from django.shortcuts import render

def porto(request):
    return render(request, 'index.html')

