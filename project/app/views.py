

from django.shortcuts import render
from django.http import HttpResponse
def app(request):
    return HttpResponse("welcome")

