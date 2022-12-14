from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
posts = [
    {
        'author': 'Aryan',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Arjun',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'August 28, 2018'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})