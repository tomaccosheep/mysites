from django.shortcuts import render
from django.utils import timezone
from .models import Post_mole

def post_list_hamster(request):
    posts = Post_mole.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list_hawk.html', {'posts_lizard': posts})

# Create your views here.
