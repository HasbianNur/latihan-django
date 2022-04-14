from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "index.html")


def buku(request):
    return render(request, "buku.html")


def user(request):
    return render(request, "user.html")


def komentar(request):
    return render(request, "komentar.html")
