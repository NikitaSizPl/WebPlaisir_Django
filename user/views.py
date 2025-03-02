from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from user.forms import UserLoginForm, UserRegisterForm, UserProfilerForm
from django.contrib import auth, messages


# Create your views here.
@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfilerForm(instance=user, data=request.POST)
        if form.is_valid():
            form.save()
    context = {
        "user": user,
    }
    return render(request, 'user/profile.html', context)


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('user:profile')
            else:
                messages.error(request, "Неверное имя пользователя или пароль")
                return redirect('user:profile')
    else:
        form = UserLoginForm()
    context = {
        'form': form
    }
    return render(request, 'user/profile.html', context)


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('user:profile')
    else:
        form = UserRegisterForm()
    context = {
        "form": form
    }
    return render(request, 'user/register.html', context)


def logout(request):
    auth.logout(request)
    return redirect('products:index')