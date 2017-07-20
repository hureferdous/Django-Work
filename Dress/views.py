from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>This is Tinua Dress App Page</h1>")