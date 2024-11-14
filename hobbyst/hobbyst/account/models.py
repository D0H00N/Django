from django.contrib.auth.models import AbstractUser
from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.

class User(AbstractUser):
    profile_image = models.ImageField(
        "프로필 이미지", upload_to='account/profile', blank=True, null=True
    )
    short_description =models.TextField('소개글', blank=True)
    preference_choices = [
        ('sports', '스포츠'),
        ('travel', '여행'),
        ('cook', '요리'),
        ('food', '맛집탐방'),
        ('fashion', '패션'),
        ('books', '독서'),
        ('music', '음악'),
        ('friends', '사교'),
        ('etc', '이외'),
    ]
    preference = MultiSelectField(choices=preference_choices, max_choices=5, max_length=100, null=True, blank=True)

    following = models.ManyToManyField(
        'self',
        verbose_name='팔로우 중인 사용자들',
        related_name='followers',
        symmetrical=False,
        through='account.Relationship'
    )

    like_posts = models.ManyToManyField(
        "board.Post",
        verbose_name="좋아요 누른 Post목록",
        related_name="like_users",
        blank=True,
    )

    def __str__(self):
        return self.username

class Relationship(models.Model):
    from_user = models.ForeignKey(
        'account.User',
        verbose_name='팔로우를 요청한 사용자',
        related_name='following_relationships',
        on_delete=models.CASCADE,
    )
    to_user = models.ForeignKey(
        'account.User',
        verbose_name='팔로우 요청의 대상',
        related_name='follower_relationships',
        on_delete=models.CASCADE,
    )
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'관계 ({self.from_user} -> {self.to_user})'
