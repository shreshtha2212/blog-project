from django.urls import path
from . import views

urlpatterns = [
    path("blogentry/", views.blog),
    path("postdetails/", views.postdetails),
    path("addblog/", views.Addblog.as_view()),
    path("api/", views.ApiView.as_view())
]