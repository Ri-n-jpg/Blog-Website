from django.shortcuts import render, get_object_or_404, redirect
from django.utils.text import slugify
from .models import Blog, Comment, Contact,Category
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

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
    print("SEARCH QUERY:", query)

    return render(request, 'home.html', {'blogs': blogs})


# 📄 Blog Detail Page
def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)

    # Optional: increase views 🔥
    blog.views += 1
    blog.save()
    comments = blog.comments.all().order_by('-created_at')

    if request.method == 'POST':
        name = request.POST.get('name')
        text = request.POST.get('text')
        Comment.objects.create(
            blog=blog,
            name=name,
            text=text
        )
        return redirect('blog_detail', slug=slug)

    return render(request, 'blog_detail.html', {'blog': blog, 'comments': comments})


# ℹ️ About Page
def about(request):
    return render(request, 'about.html')


# 📞 Contact Page
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(name, email, message)
        return render(request, 'contact.html', {'success': True})
    return render(request, 'contact.html')


# ✏️ Edit Blog (login required)
@login_required
def edit_blog(request, slug):
    blog = get_object_or_404(Blog, slug=slug)

    # ✅ Only author can edit
    if request.user != blog.author:
        return redirect('home')

    if request.method == "POST":
        blog.title = request.POST.get('title')
        blog.blog_body = request.POST.get('blog_body')
        blog.save()
        return redirect('blog_detail', slug=blog.slug)

    return render(request, 'edit_blog.html', {'blog': blog})


# 🗑️ Delete Blog (login required)
@login_required
def delete_blog(request, slug):
    blog = get_object_or_404(Blog, slug=slug)

    # ✅ Only author can delete
    if request.user != blog.author:
        return redirect('home')

    blog.delete()
    return redirect('home')


# 👤 Signup View
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
@login_required
def create_blog(request):
    if request.method == "POST":
        title = request.POST.get('title')
        category_id = request.POST.get('category')
        image = request.FILES.get('featured_image')
        short_description = request.POST.get('short_description')
        blog_body = request.POST.get('blog_body')
        status = request.POST.get('status')

        slug = slugify(title)

        blog = Blog.objects.create(
            title=title,
            slug=slug,
            category_id=category_id,
            author=request.user,
            featured_image=image,
            short_description=short_description,
            blog_body=blog_body,
            status=status
        )

        return redirect('blog_detail', slug=blog.slug)

    categories = Category.objects.all()
    return render(request, 'create_blog.html', {'categories': categories})
from django.contrib.auth.models import User

def profile(request, username):
    user = User.objects.get(username=username)
    blogs = Blog.objects.filter(author=user)

    return render(request, 'profile.html', {
        'profile_user': user,
        'blogs': blogs
    })
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def like_blog(request, slug):
    if request.method == "POST":
        blog = get_object_or_404(Blog, slug=slug)

        # Toggle like for demonstration (simple count)
        blog.likes += 1
        blog.save()
        return JsonResponse({"likes": blog.likes})
    return JsonResponse({"error": "Invalid request"}, status=400)