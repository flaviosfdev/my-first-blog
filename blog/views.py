from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.

def post_list(request):
    posts = Post.objects.order_by('published_date')
    return render(request = request, template_name = 'blog/post_list.html', context = {'posts':posts})