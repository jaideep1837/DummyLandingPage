from django.http import HttpResponse
from django.shortcuts import render
from api.models import Service

def homepage(request):
    username = request.POST.get('usern')
    password = request.POST.get('passn')
    if username!=None and password!=None:
        if Service.objects.filter(username=username).exists():
            return render(request, "failure.html")
        else:
            Service(username=username, password=password).save()
            return render(request, "success.html")

    return render(request, "index.html")