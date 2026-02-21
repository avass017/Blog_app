from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from blog_app.forms import UsersRegister, LoginRegister
from blog_app.models import Users


# Create your views here.

def index(request):
    return render(request, 'indexc.html')

def login_page(request):
    return render(request,'login.html')
def dashboard(request):
    return render(request,'dashboard.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if user.is_staff:
                return redirect('admin')
            else:
                return redirect('users')

        else:
            messages.info(request, 'invalid credentials')

    return render(request, 'login.html')

def users(request):
    return render(request,'users/dash.html')
def admin(request):
    return render(request,'admin/admin_dash.html')


def users_add(request):
    if request.method == "POST":
        use_form = UsersRegister(request.POST, request.FILES)
        login_form = LoginRegister(request.POST)

        if use_form.is_valid() and login_form.is_valid():
            use = login_form.save(commit=False)
            use.is_users = True
            use.save()

            user = use_form.save(commit=False)
            user.users_detail = use
            user.save()


    else:
            use_form = UsersRegister()
            login_form = LoginRegister()

    return render(request,'register.html', {'use_form': use_form, 'login_form': login_form})

