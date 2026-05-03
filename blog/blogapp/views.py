from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.utils.text import slugify

from .models import Blog, Comment, Contact, Category


# 🏠 HOME PAGE
def home(request):
    query = request.GET.get('q')

    blogs_list = Blog.objects.filter(status="Published").order_by('-created_at')

    if query:
        blogs_list = blogs_list.filter(
            Q(title__icontains=query) | Q(blog_body__icontains=query)
        )

    trending_blogs = Blog.objects.filter(
        status="Published",
        views__gt=10
    ).order_by('-views', '-created_at')[:5]

    paginator = Paginator(blogs_list, 6)
    page_number = request.GET.get('page')
    blogs = paginator.get_page(page_number)

    return render(request, 'home.html', {
        'blogs': blogs,
        'trending_blogs': trending_blogs
    })


# 📄 BLOG DETAIL
def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)

    blog.views += 1
    blog.save()

    comments = blog.comments.all().order_by('-created_at')

    if request.method == 'POST':
        Comment.objects.create(
            blog=blog,
            name=request.POST.get('name'),
            text=request.POST.get('text')
        )
        return redirect('blog_detail', slug=slug)

    return render(request, 'blog_detail.html', {
        'blog': blog,
        'comments': comments
    })


# ℹ️ ABOUT
def about(request):
    return render(request, 'about.html')


# 📞 CONTACT
def contact(request):
    if request.method == "POST":
        Contact.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            message=request.POST.get('message')
        )
        return render(request, 'contact.html', {'success': True})

    return render(request, 'contact.html')


# ✏️ EDIT BLOG
@login_required
def edit_blog(request, slug):
    blog = get_object_or_404(Blog, slug=slug)

    if request.user != blog.author:
        return redirect('home')

    if request.method == "POST":
        blog.title = request.POST.get('title')
        blog.blog_body = request.POST.get('blog_body')
        blog.save()
        return redirect('blog_detail', slug=blog.slug)

    return render(request, 'edit_blog.html', {'blog': blog})


# 🗑️ DELETE BLOG
@login_required
def delete_blog(request, slug):
    blog = get_object_or_404(Blog, slug=slug)

    if request.user != blog.author:
        return redirect('home')

    blog.delete()
    return redirect('home')


# 👤 SIGNUP
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})


# 📝 CREATE BLOG (FIXED CATEGORY ISSUE)
@login_required
def create_blog(request):
    categories = Category.objects.all()

    if request.method == "POST":
        title = request.POST.get('title')
        category_id = request.POST.get('category')
        image = request.FILES.get('featured_image')
        short_description = request.POST.get('short_description')
        blog_body = request.POST.get('blog_body')
        status = request.POST.get('status')

        # 🚨 VALIDATION
        if not title:
            return HttpResponse("Title is required")

        if not category_id:
            return HttpResponse("Category is required")

        category = get_object_or_404(Category, id=category_id)

        Blog.objects.create(
            title=title,
            slug=slugify(title),
            category=category,
            author=request.user,
            featured_image=image,
            short_description=short_description,
            blog_body=blog_body,
            status=status
        )

        return redirect('home')

    return render(request, 'create_blog.html', {
        'categories': categories
    })


# 👤 PROFILE
def profile(request, username):
    profile_user = get_object_or_404(User, username=username)

    blogs = Blog.objects.filter(author=profile_user)
    saved_blogs = profile_user.saved_blogs.all()

    return render(request, 'profile.html', {
        'profile_user': profile_user,
        'blogs': blogs,
        'saved_blogs': saved_blogs
    })


# ❤️ LIKE BLOG
@csrf_exempt
def like_blog(request, slug):
    if request.method == "POST":
        blog = get_object_or_404(Blog, slug=slug)
        blog.likes += 1
        blog.save()
        return JsonResponse({"likes": blog.likes})

    return JsonResponse({"error": "Invalid request"}, status=400)


# 💾 SAVE BLOG
@login_required
def save_blog(request, slug):
    blog = get_object_or_404(Blog, slug=slug)

    if request.user in blog.saved_by.all():
        blog.saved_by.remove(request.user)
        saved = False
    else:
        blog.saved_by.add(request.user)
        saved = True

    return JsonResponse({
        'saved': saved,
        'total_saved': blog.saved_by.count()
    })