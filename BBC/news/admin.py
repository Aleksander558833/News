from django.contrib import admin
from .models import Category, Post
#
class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'title']
    list_filter = ('author', 'category')
    search_fields = ('name', 'time_in')
#
admin.site.register(Category)
admin.site.register(Post, PostAdmin)