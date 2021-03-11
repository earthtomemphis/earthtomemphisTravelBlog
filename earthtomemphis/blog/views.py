from django.db import models
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Category, Post
from .forms import PostForm
# Create your views here.


class ArticleListView(ListView):
    model = Post
    template_name = 'index.html'
    paginate_by = 3


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    context_object_name = 'post'

    def get_success_url(self):
        return reverse('article-detail', kwargs={'slug': self.object.slug})


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats)
    return render(request, 'categories.html', {'cats': cats.title(), 'category_post': category_posts})


class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'
    context_object_name = 'post'


class UpdatePostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'update_post.html'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('index')
