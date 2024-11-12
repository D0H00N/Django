from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    if not request.user.is_authenticated:
        return redirect('/account/login')

    return render(request, 'board/home.html')