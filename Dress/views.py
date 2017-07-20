from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
import datetime


def index(request):
    all_cloths = Cloth.Objects.all()
    template = loder.get_template(' ')
    return HttpResponse(' ')

def detail(request,Cloth_id):
    return HttpResponse("<h2>Details For The Dress" + str(Cloth_id) + "</h2>")

def say_hello(request):
    name = "My_first_site"
    html = "<html> <body><h1>Hello %s !!!!!</h1></body></html>" %name
    return HttpResponse(html)

def get_now(request):
    now = datetime.datetime.now()
    return render(request, "HelloWorld/base.html", {"current_date":now})
