from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from account.forms import LoginForm, SignupForm
from account.models import User
from rest_framework import status, generics, mixins#, viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import RegisterSerializer

# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        return redirect("board:home")

    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect("board:home")
            else:
                # print('로그인에 실패했습니다')
                form.add_error(None, "입력한 자격증명에 해당하는 사용자가 없습니다")

        context = {"form": form}
        return render(request, "account/login.html", context)
    else:
        form = LoginForm()
        context = {"form": form}
        return render(request, "account/login.html", context)


def logout_view(request):
    logout(request)
    return redirect("account:login")


def signup(request):
    if request.method == "POST":
        form = SignupForm(data=request.POST, files=request.FILES)

        if form.is_valid():
            user = form.save()
            # login(request, user) ## 회원가입 후 로그인 한 뒤 들어가도록
            return redirect("account:login")
        else:
            context = {"form": form}
            return render(request, "account/signup.html", context)
    else:
        form = SignupForm()

    context = {"form": form}
    return render(request, "account/signup.html", context)


def profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    context = {
        "user": user,
    }
    return render(request, "account/profile.html", context)


def followers(request, user_id):
    user = get_object_or_404(User, id=user_id)
    relationships = user.follower_relationships.all()
    context = {
        "user": user,
        "relationships": relationships,
    }
    return render(request, "account/followers.html", context)


def following(request, user_id):
    user = get_object_or_404(User, id=user_id)
    relationships = user.following_relationships.all()
    context = {
        "user": user,
        "relationships": relationships,
    }
    return render(request, "account/following.html", context)


def follow(request, user_id):

    user = request.user

    target_user = get_object_or_404(User, id=user_id)

    if target_user in user.following.all():
        user.following.remove(target_user)

    else:
        user.following.add(target_user)

    url_next = request.GET.get("next") or reverse("account:profile", args=[user.id])
    return HttpResponseRedirect(url_next)

class RegisterUsers(APIView):
   def get(self, request):
        users = User.objects.all()
        serializer = RegisterSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        