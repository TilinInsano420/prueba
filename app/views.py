from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def hola (request):
    render(request,'/app/index.html')

def hola2 (request):
    render(request,'/app/pagina.html')