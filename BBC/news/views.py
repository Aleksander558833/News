from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
from .filters import PostFilter
from .forms import PostForm
from django.contrib.auth.mixins import PermissionRequiredMixin

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
        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'Post'

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