from django.shortcuts import render
from django.http import HttpResponse

def practice(request):
    return HttpResponse("성공!")

def number(request, number):
    return HttpResponse(f"{number}")