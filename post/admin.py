from django.contrib import admin
from .models import Post

# Define a custom admin class for the Post model
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'created_at')  # Include 'created_at' in the list_display

# Register the Post model with the custom admin class
admin.site.register(Post, PostAdmin)