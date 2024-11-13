from django.contrib.auth.models import AbstractUser
from django.db import models

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
    preference = models.CharField(max_length=20, choices=preference_choices, null=True, blank=True)