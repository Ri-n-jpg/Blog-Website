from django.contrib import admin
from .models import Category, Blog, Contact
from django.utils import timezone
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'category', 'author', 'is_featured', 'status', 'created_at')
    list_filter = ('category', 'status', 'is_featured')  # optional filters
    search_fields = ('id', 'title', 'category__category_name', 'status')
    list_editable = ('is_featured',)
admin.site.register(Category)
admin.site.register(Blog,BlogAdmin)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','message','created_at')
admin.site.register(Contact,ContactAdmin)
# Register your models here.
actions = ['mark_as_read']

def mark_as_read(self, request, queryset):
    queryset.update(is_read=True)

mark_as_read.short_description = "Mark selected messages as Read"
