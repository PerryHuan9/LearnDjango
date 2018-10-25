from django.shortcuts import render
from django.http import HttpResponse, Http404


def index(request):
    return HttpResponse('<h1 style="text-align:center;">我是index</h1>')
