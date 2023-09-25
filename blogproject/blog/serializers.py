from rest_framework.serializers import ModelSerializer
from .models import AddBlog

class BlogSerialiazer(ModelSerializer):

    class Meta:
        model = AddBlog
        fields = ['title', 'post']
