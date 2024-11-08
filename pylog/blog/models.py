from django.db import models

# Create your models here.
class Post(models.Model): # ORM 기능 사용
    title = models.CharField("포스트제목", max_length=100) #짧은 글
    content = models.TextField("포스트 내용") #긴 글
    thumbnail = models.ImageField("썸네일 이미지", upload_to="post", blank=True)
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE) #1:N 관계 정의key
    content = models.TextField("댓글 내용")    #^같이 삭제되어라

    def __str__(self):
        return f"{self.post.title}의 댓글 (ID: {self.id})"