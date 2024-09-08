from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post, Subscription, Category
from .filters import PostFilter
from .forms import PostForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Exists, OuterRef
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.core.cache import cache
from django.utils.timezone import timezone
from datetime import datetime

import pytz

class PostList(ListView):
    model = Post
    # ordering = 'category'
    template_name = 'News.html'
    context_object_name = 'news'
    ordering = '-time_in'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        context = {
            'current_time': timezone.localtime(timezone.now()),
            'timezones': pytz.common_timezones  # добавляем в контекст все доступные часовые пояса
        }
        return context

    def post(self, request):
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('/')

class PostDetail(DetailView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'Post'

    def get_object(self, *args, **kwargs):
        obj = cache.get(f'Post-{self.kwargs["pk"]}', None)

        if not obj:
            obj = super().get_object(queryset=self.queryset)
            cache.set(f'Post-{self.kwargs["pk"]}', obj)
        return obj

class NewsCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post')
    form_class = PostForm
    model = Post
    template_name = 'news_create.html'

    def from_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user.author

        if 'news/create' in self.request.path:
            post.field = 'NE'
        else:
            post.field = 'AR'
        return super().form_valid(form)

class NewsUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_post')
    form_class = PostForm
    model = Post
    template_name = 'news_create.html'

class NewsDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_post')
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('post_list')

class ArticleCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_article')
    form_class = PostForm
    model = Post
    template_name = 'article_create.html'

class ArticleUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_article')
    form_class = PostForm
    model = Post
    template_name = 'article_create.html'

class ArticleDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_article')
    model = Post
    template_name = 'article_delete.html'
    success_url = reverse_lazy('post_list')


@login_required
@csrf_protect
def subscriptions(request):
    if request.method == 'POST':
        category_id = request.POST.get('category_id')
        category = Category.objects.get(id=category_id)
        action = request.POST.get('action')

        if action == 'subscribe':
            Subscription.objects.create(user=request.user, category=category)
        elif action == 'unsubscribe':
            Subscription.objects.filter(
                user=request.user,
                category=category,
            ).delete()

    categories_with_subscriptions = Category.objects.annotate(
        user_subscribed=Exists(
            Subscription.objects.filter(
                user=request.user,
                category=OuterRef('pk'),
            )
        )
    ).order_by('name')
    return render(
        request,
        'subscriptions.html',
        {'categories': categories_with_subscriptions},
    )