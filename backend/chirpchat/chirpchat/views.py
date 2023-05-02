from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse


def home(request):
    return HttpResponse("This is Home Page")