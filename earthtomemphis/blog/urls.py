from django.urls import path
from .views import AddCategoryView, ArticleListView, AddPostView, ArticleDetailView, UpdatePostView, DeletePostView, CategoryView

urlpatterns = [
    path('', ArticleListView.as_view(), name='index'),
    path('article/add/post/', AddPostView.as_view(), name='add-post'),
    path('article/add/category/', AddCategoryView.as_view(), name='add-category'),
    path('article/<slug:slug>/', ArticleDetailView.as_view(), name='article-detail'),
    path('article/<slug:slug>/update/',
         UpdatePostView.as_view(), name='update-post'),
    path('article/<slug:slug>/delete/',
         DeletePostView.as_view(), name='delete-post'),
    path('category/<str:cats>', CategoryView, name='category'),
]
