from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post 

# Decorator for login checking
@login_required(login_url='/accounts/login_user/')
def create_post(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['url']:
            # Instantiate new post
            post = Post()

            # Initialize fields
            post.title = request.POST['title']

            # Appaned url with http/https if not already there
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                post.url = request.POST['url']
            else:
                post.url = 'https://' + request.POST['url']

            post.pub_date = timezone.datetime.now()
            post.author = request.user

            # Save to database
            post.save() 
            return redirect('home')
        else:
            return render(request, 'posts/create_post.html', {'error': 'Whoa! Posts must contain both a title and a URL'})
    else:
        return render(request, 'posts/create_post.html')

def home(request):
    posts = Post.objects.order_by('-votes_total')

    return render(request, 'posts/home.html', {'posts': posts})

def upvote(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(pk = pk)

        # upboat increment
        post.votes_total += 1
        post.save()

        return redirect('home')

def downvote(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(pk = pk)

        # upboat increment
        post.votes_total -= 1
        post.save()

        return redirect('home')


def posts_by_user(request):
    return render(request, 'posts/posts_by_user.html')