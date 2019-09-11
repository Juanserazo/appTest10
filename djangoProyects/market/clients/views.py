from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse(" ############ You are in the index file ###############")

def hello(request):
    return HttpResponse("::::::::This is another message::::::::::")

def listClients(request):
    return HttpResponse(" HERE YOU MUST LIST THE CLIENTS IN DB   ")
