
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests


# Create your views here.


def app(request):
    if request.method == 'POST':
        print(request)
        user = request.POST['username']
        blg = request.POST['blog']
        return JsonResponse({'success': '200'})

        print(user)
        print(blg)

    else:
        return render(request, 'index.html')
