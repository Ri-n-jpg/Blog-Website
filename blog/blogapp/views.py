from django.shortcuts import render, get_object_or_404
from .models import Blog

# 🏠 Home Page
def home(request):
    blogs = Blog.objects.filter(status="Published")
    return render(request, 'home.html', {'blogs': blogs})


# 📄 Blog Detail Page
def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)

    # Optional: increase views 🔥
    blog.views += 1
    blog.save()

    return render(request, 'blog_detail.html', {'blog': blog})


# ℹ️ About Page
def about(request):
    return render(request, 'about.html')


# 📞 Contact Page
def contact(request):
    return render(request, 'contact.html')