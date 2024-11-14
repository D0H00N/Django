from django.urls import path
from board.views import home, comment_add, comment_delete, post_add, tags

app_name = 'board'
urlpatterns = [
    path('', home, name='home'),
    path("comment_add/", comment_add, name="comment_add"),
    path("comments/<int:comment_id>/delete/", comment_delete, name="comment_delete"),
    path("post_add/", post_add, name="post_add"),
    path("tags/<str:tag_name>/", tags, name="tags"),
]