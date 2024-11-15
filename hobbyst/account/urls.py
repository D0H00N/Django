from django.urls import path
from account.views import (
    login_view,
    logout_view,
    signup,
    profile,
    followers,
    following,
    follow,
)

app_name = "account"
urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("signup/", signup, name="signup"),
    path("<int:user_id>/profile/", profile, name="profile"),
    path("<int:user_id>/followers/", followers, name="followers"),
    path("<int:user_id>/following/", following, name="following"),
    path("<int:user_id>/follow/", follow, name="follow"),
]
