from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User, Group
from django.shortcuts import redirect, render

from .forms import CreateUserForm
from .models import Guest


def user_create(request):
    pass


def user_login(request):
    if request.user.is_authenticated:
        role = f"{request.user.groups.all()[0]}"
        path = role + '/'
        return redirect(f"/{path}")
    else:
        if request.method == 'POST':
            username, password = [request.POST.get('username'), request.POST.get('password')]
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                role = f"{request.user.groups.all()[0]}"
                path = role + "/"
                return redirect(f"/manager")
        return render(request, 'users/login.html')


def user_logout(request):
    logout(request)
    return redirect('/')


def guest_create(request):
    form = CreateUserForm()
    if request.user.is_authenticated:
        role = f"{request.user.groups.all()[0]}"
        path = role + '/'
        if role == 'guest':
            return redirect('/')
        elif role == 'manager':
            return redirect(f"/{role}")
    else:
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                if len(User.objects.filter(email=request.POST.get('email'))) != 0:
                    messages.error(request, 'Email already taken!')
                    return redirect('/user/guest-create')
                user = form.save()
                group = Group.objects.get(name='guest')
                user.groups.add(group)
                guest = Guest(user=user, phone_number=request.POST.get('phoneNumber'))
                guest.save()
                messages.success(request, 'Guest account created. Welcome Abort!')

                return redirect('/user/login')
        context = {
            'form': form
        }
        return render(request, 'users/guest.create.html', context)
