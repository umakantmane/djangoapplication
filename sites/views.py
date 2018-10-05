from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from sites.forms import LoginForm,SignupUser


def userLogin(request):

    if request.user.username:
        return redirect(home)

    message = ''
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(
                username=username,
                password=password
            )

            if user is None:
                message = 'Invalid user!'
            else:

                login(request, user)
                request.session['phone'] = '123456789'
                request.session['pincode'] = '585328'

                return redirect(home)

    return render(
        request,
        'auth_user/login.html',{
            'form':form,
            'msg':message
        }
    )

def userRegitser(request):

    if request.user.username:
        return redirect(home)

    message = ''
    form = SignupUser()
    if request.method == 'POST':
        form = SignupUser(request.POST)
        if form.is_valid():

            user = User()
            user.username = form.cleaned_data['username']
            user.email = form.cleaned_data['email']
            user.set_password(form.cleaned_data['password1'])
            #user.password = form.cleaned_data['password1']
            user.save()

            message = 'Registration done successfully!'
    return render(
        request,
        'auth_user/signup.html',{
        'form':form,
        'msg':message
        }
    )

def home(request):

    return render(request, 'auth_user/home.html')

def userLogout(request):

    logout(request)
    return redirect(home)