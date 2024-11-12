from django.urls import path
from account.views import login_view,logout_view,signup

urlpatterns = [
    path("login/", login_view),
    path("logout/", logout_view),
    path("signup/", signup),
]