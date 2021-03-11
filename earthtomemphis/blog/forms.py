from django import forms
from .models import Post, Category

choices = Category.objects.all().values_list('name', 'name')

category_list = []

for item in choices:
    category_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title',
            'slug',
            'author',
            'category',
            'body',
            'status',
            'metades'
        )

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=category_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'metades': forms.TextInput(attrs={'class': 'form-control'}),
        }
