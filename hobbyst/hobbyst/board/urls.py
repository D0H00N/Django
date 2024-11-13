from django.urls import path
from board.views import home
# , post_write, comment_add

urlpatterns = [
    path('', home, name='home'),
    # path('post_write/', post_write),
    # path('comment_add/', comment_add, name='comment_add'),
]