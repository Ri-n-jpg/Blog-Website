# blog/urls.py (app urls)

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('blog/edit/<slug:slug>/', views.edit_blog, name='edit_blog'),
    path('blog/delete/<slug:slug>/', views.delete_blog, name='delete_blog'),
path('create/', views.create_blog, name='create_blog'),
path('create-blog/', views.create_blog, name='create_blog'),
]