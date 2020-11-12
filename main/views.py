from django.shortcuts import render
from django.http import HttpResponse
from .models import User


# Create your views here.


def index(response):
    return render(response, "main/base.html", {})


def home(response):
    return render(response, "main/home.html", {})
