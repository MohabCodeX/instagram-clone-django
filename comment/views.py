from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from .models import Comment

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.user == request.user:
        post_id = comment.post.id  # Get the regular post ID
        comment.delete()
        messages.success(request, 'Comment deleted successfully')
    return redirect('post-details', post_id)  # Using 'post-details' to match your URL pattern
