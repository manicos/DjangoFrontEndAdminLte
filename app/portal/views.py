from django.shortcuts import render
import urllib,json

# Create your views here.
from django.http import HttpResponse, JsonResponse

def index(request):
    return render(request, 'index.html')

def list(request):

    response1 = urllib.request.urlopen('https://rickandmortyapi.com/api/character')
    data = json.loads(response1.read())
    results = data["results"]

    context = {
        "data" :  results,
    }

    return render(request, 'list.html', context)
