from django.urls import path
from account.views import (login_view,logout_view,signup,
                        profile,followers,following,
                        follow,RegisterUsers)

app_name = "account"
urlpatterns = [
    path("login/", login_view.as_view(), name="login"),
    path("logout/", logout_view.as_view(), name="logout"),
    path("signup/", signup.as_view(), name="signup"),
    path("<int:user_id>/profile/", profile.as_view(), name="profile"),
    path("<int:user_id>/followers/", followers.as_view(), name="followers"),
    path("<int:user_id>/following/", following.as_view(), name="following"),
    path("<int:user_id>/follow/", follow.as_view(), name="follow"),
    path('registerusers/', RegisterUsers.as_view()),
]

AUTH_USER_MODEL = 'accounts.User'