from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(
        published_date__isnull=False,
        # published_date__lte=timezone.now()
    ).order_by('published_date')
    return render(request = request, template_name = 'blog/post_list.html', context = {'posts':posts})