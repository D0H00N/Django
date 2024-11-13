from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from account.forms import LoginForm, SignupForm
from account.models import User

# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        return redirect('/board/')
    
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user :
                login(request, user)
                return redirect('/board/')
            else:
                # print('로그인에 실패했습니다')
                form.add_error(None, "입력한 자격증명에 해당하는 사용자가 없습니다")

        context = {'form':form}
        return render(request, 'account/login.html', context)
    else:
        form = LoginForm()
        context = {'form':form}
        return render(request, 'account/login.html', context)
    

def logout_view(request):
    logout(request)
    return redirect('/account/login')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(data=request.POST, files=request.FILES)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/board/')
        else:
            context = {'form':form}
            return render(request, 'account/signup.html', context)
    else:
        form = SignupForm()
        
    context = {'form':form}
    return render(request, 'account/signup.html', context)
    # form = SignupForm()
    # context = {'form':form}
    # return render(request, 'account/signup.html', context)