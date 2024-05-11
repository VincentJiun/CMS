from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm # Django 內建UserCreationForm 表單
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
# Create your views here.

def user_profile(request):
    return render(request, 'account/profile.html')

def user_register(request):
    form = UserCreationForm()
    msg = ''
    if request.method == 'POST':
        
        print(request.POST)
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # 密碼檢查
        if password1 != password2:
            msg = '密碼確認不一致!!!'
        # 密碼過短
        elif len(password1) < 8:
            msg = '密碼過短(少於8個字元)'
        # 帳號問題 (使用者已存在)   
        elif User.objects.filter(username=username).exists():
            msg = '帳號已存在!!!'
        else:
            user = User.objects.create_user(username=username, password=password1)
            if user is not None:
                user.save()
                msg = '註冊成功'
                login(request, user)
                return redirect('todo')

    return render(request, 'account/register.html', {'form': form, 'msg': msg})

def user_login(request):
    msg = ''
    if request.method == 'POST':
        if request.POST.get('register'):
            return redirect('register')
        
        elif request.POST.get('login'):
            username = request.POST.get('username')
            password = request.POST.get('password')

            if username == '' or password == '':
                msg = '帳號/密碼不能為空!!!'
            else:
                user = authenticate(request, username=username, password=password) # Django 內建使用者驗證功能
                if not user:
                    msg = 'Invalid username or password'
                else:
                    msg = '登入成功'
                    login(request, user) # Django 內建登入功能
                    return redirect('todo')

    return render(request, 'account/login.html', {'msg': msg})

def user_logout(request):
    logout(request)
    return redirect('login')