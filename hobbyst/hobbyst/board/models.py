from django.db import models

# Create your models here.

class Board(models.Model):
    user = models.ForeignKey(
        "account.User",verbose_name="작성자", on_delete=models.CASCADE,
    )
    content = models.TextField("내용")
    created = models.DateTimeField("생성일시", auto_now_add=True)

class BoardImage(models.Model):
    board = models.ForeignKey(
        Board,verbose_name="보드",on_delete=models.CASCADE,
    )
    photo = models.ImageField("사진", upload_to="board")

class Comment(models.Model):
    user = models.ForeignKey(
        "account.User", verbose_name="작성자", on_delete=models.CASCADE,
    )
    board = models.ForeignKey(Board,verbose_name="보드",on_delete=models.CASCADE)
    content = models.TextField("내용")
    created = models.DateTimeField("생성일시", auto_now_add=True)
