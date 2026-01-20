from django.shortcuts import render
from blog.models import Post
def home(request):
    latest = Post.objects.order_by('-created')[:5]
    return render(request, 'core/home.html', {'latest': latest})
