from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Post

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user  # Set the user to the currently logged-in user
            post.save()
            return redirect("post_all")  # Redirect to the post detail view
    else:
        form = PostForm()
    
    return render(request, 'create.html', {'form': form})

@login_required
def post_all(request):
    posts = Post.objects.all()  # Retrieve all posts from the database
    return render(request, 'post_all.html', {'posts': posts})

@login_required
def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post.html', {'post': post})