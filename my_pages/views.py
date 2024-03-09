from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render



def home(request):
    return HttpResponse('<h1 style="color:red">Home section</h1><br><a href="../about">About section</a>')


def about(request):
    return HttpResponse('<h1 style="color:green">About section</h1><br><a href="../home">Home section</a><br><a href="../test">Test section</a>')

def test(request):
    return HttpResponse('<h1 style="color:blue">Test section</h1><br><a href="../about">About section</a><br><a href="../help">Help section</a>')


def help(request):
    return HttpResponse('<h1 style="color:yellow">Help section</h1><br><a href="../test">Test section</a><br><a href="../django">Django section</a>')

def django(request):
    return HttpResponse('<h1 style="color:orange">Django section</h1><br><a href="../help">Help section</a>')


