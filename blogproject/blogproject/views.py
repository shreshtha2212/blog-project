from django.http import HttpResponse 

def index(request):
    return HttpResponse("Hello World")

def home(request):
    return HttpResponse("<h1 style='color:red'>Hello this is your home</h1>")

def showname(request, name):
    return HttpResponse(f"<h1>Welcome {name}</h1>")