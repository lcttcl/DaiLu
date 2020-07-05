from django.shortcuts import render, redirect, reverse

# Create your views here.
from django.shortcuts import render
from .forms import UserRegisterForm
from .models import UserProfile
from django.db.models import Q


def index(request):
    return render(request, 'index.html')


def user_register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        user_register_form = UserRegisterForm(request.POST)
        if user_register_form.is_valid():
            username = user_register_form.cleaned_data['username']
            email = user_register_form.cleaned_data['email']
            password = user_register_form.cleaned_data['password']
            password_confirm = user_register_form.cleaned_data['password_confirm']
            user_list = UserProfile.objects.filter(email=email)
            if user_list:
                return render(request, 'register.html', {
                    'msg': "邮箱已存在",
                })
            elif password != password_confirm:
                return render(request, 'register.html', {
                    'msg': "两次密码不一致",
                })
            else:
                a = UserProfile()
                a.username = username
                a.email = email
                a.set_password(password)
                a.save()
                return redirect(reverse('index'))
        else:
            return render(request, 'register.html', {
                'user_register_form': user_register_form,
            })

def user_login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    else:
        pass

