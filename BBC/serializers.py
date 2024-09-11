from news.models import Post, Category, Author, User
from rest_framework import serializers

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'field', 'category', 'author', 'time_in', 'title', 'text']

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'field', 'category', 'author', 'time_in', 'title', 'text']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'user']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']