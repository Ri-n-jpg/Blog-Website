from django.shortcuts import render, get_object_or_404
from .models import Blog
from .models import Contact
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import  redirect

# 🏠 Home Page
def home(request):
    query = request.GET.get('q')
    blogs_list = Blog.objects.filter(status="Published").order_by()
    if query:
        blogs_list = blogs_list.filter(
            Q(title__icontains=query) | Q(blog_body__icontains=query)
        )
    paginator = Paginator(blogs_list, 6)
    page_number = request.GET.get('page')
    blogs = paginator.get_page(page_number)

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
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        print(name,email,message)
        return render(request, 'contact.html',{'success':True})
    return render(request,'contact.html')
from django.shortcuts import redirect

def edit_blog(request, slug):
    blog = Blog.objects.get(slug=slug)

    if request.method == "POST":
        blog.title = request.POST.get('title')
        blog.blog_body = request.POST.get('blog_body')
        blog.save()

        return redirect('blog_detail', slug=blog.slug)

    return render(request, 'edit_blog.html', {'blog': blog})

def delete_blog(request, slug):
    blog = Blog.objects.get(slug=slug)
    blog.delete()
    return redirect('home')