from django.contrib import admin
from blog.models import Post, Comment
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','content','thumbnail']
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass