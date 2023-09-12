from django.shortcuts import render, redirect
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user  # Set the user to the currently logged-in user
            post.save()
            # return redirect('post_detail', pk=post.pk)  # Redirect to the post detail view
    else:
        form = PostForm()
    
    return render(request, 'create.html', {'form': form})
