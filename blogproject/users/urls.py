from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index),  # '' --> domain/users/ now changed to domain
    path("about/", views.about),
    path("contact/", views.contact),
    path("signup/", views.signup),
    path("aftersignup/", views.aftersignup),
    path('login/', views.login),
    path("afterlogin/", views.Afterlogin.as_view()),
    path("logout/", views.logout),
    path("blog/", include("blog.urls"))
]