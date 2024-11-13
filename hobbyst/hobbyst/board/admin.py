from django.contrib import admin
from board.models import Board,BoardImage,Comment

# Register your models here.
import admin_thumbnails

@admin_thumbnails.thumbnail("photo")
class BoardImageInline(admin.TabularInline):
    model = BoardImage
    extra = 1

 
@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ["id","content",]


@admin.register(BoardImage)
class BoardImageAdmin(admin.ModelAdmin):
    list_display = ["id","board","photo",]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["id","board","content",]

