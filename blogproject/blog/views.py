from django.shortcuts import render
from django.views import View
from users.models import User
from .models import AddBlog 
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BlogSerialiazer

# Create your views here.
def blog(request):
    blogs = AddBlog.objects.all()
    return render(request, "blog.html", {'blogs': blogs})

def postdetails(request):
    return render(request, "post-details.html")

class Addblog(View):
    def get(self, request):
        return render(request, 'post-details.html')
    
    def post(self, request):
        title = request.POST.get('title')
        post = request.POST.get('post')
        username = request.session.get('username')
        author = User.objects.get(username=username)
        AddBlog.objects.create(title=title, post=post, author=author)
        msg = "Blog Added Successfully"
        return render(request, 'post-details.html', {'msg': msg})

class ApiView(APIView):
    def get(self, request):
        all_data = AddBlog.objects.all()
        res = BlogSerialiazer(all_data, many=True)
        return Response(res.data)