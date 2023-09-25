from urllib.parse import uses_relative
from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from django.views import View

# Create your views here.
def index(request):
    # return HttpResponse("Users APP")
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def signup(request):
    return render(request, "signup.html")

def login(request):
    return render(request, 'login.html')

def aftersignup(request):
    if request.method == "GET":
        return render(request, "signup.html")
    else:
        name = request.POST.get("name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        passwd = request.POST.get("password")
        try:
            User.objects.create(name=name, username=username, email=email, password=passwd)
        except:
            msg = "username or email already exists"
            return render(request, 'signup.html', {'msg': msg})
        else: # when error will not come 
            return render(request, "login.html", {'msg': 'Successfully Registered. Login to continue'})

class Afterlogin(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get("password")
        try:
            obj = User.objects.get(username=username)
        except:
            msg = "username does not exists"
            return render(request, "login.html", {'msg': msg})
        else:
            if obj.password == password:
                request.session['islogin'] = 'true'
                request.session['username'] = username  
                return render(request, "afterlogin.html")
            else:
                msg = "password does not correct"
                return render(request, "login.html", {'msg': msg})

def logout(request):
    del request.session['islogin']
    del request.session['username']
    return render(request, 'index.html')
