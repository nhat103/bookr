from django.shortcuts import render


def index(request):
    name = "Welcom to bookr"
    return render(request, "base.html", {'name': name})


def welcome_view(request):
    return render(request, 'base.html')
