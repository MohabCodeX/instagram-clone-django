from django.urls import path
from post.views import index, NewPost, PostDetail, Tags, like, favourite
from comment import views

urlpatterns = [
    path('', index, name='index'),
   path('newpost/', NewPost, name='newpost'),
    path('<uuid:post_id>', PostDetail, name='post-details'),
    path('tag/<slug:tag_slug>', Tags, name='tags'),
    path('<uuid:post_id>/like', like, name='like'),
    path('<uuid:post_id>/favourite', favourite, name='favourite'),
    path('delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]