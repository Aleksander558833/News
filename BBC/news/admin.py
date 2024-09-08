from django.contrib import admin
from .models import Category, Post
from modeltranslation.admin import TranslationAdmin

class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'title']
    list_filter = ('author', 'category')
    search_fields = ('name', 'time_in')

class TransCategoryAdmin(TranslationAdmin):
    model = Category

class TransPostAdmin(PostAdmin, TranslationAdmin):
    model = Post

admin.site.register(Category, TransCategoryAdmin)
admin.site.register(Post, TransPostAdmin)