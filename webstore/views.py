from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.db.models import Count

# Create your views here.

def home(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request,'home.html',context)

def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        context = {}
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username = username, password = password)
            if user is not None:
                try:
                    login(request, user)
                    return redirect('home')
                except:
                    messages.success(request,"Ha ocurrido un error, intenta de nuevo")
                    return render(request,'login.html',context)
            else:
                messages.success(request,"Usuario no registrado")
                return render(request,'login.html',context)

        return render(request,'login.html',context)

def user_logout(request):
    logout(request)
    return redirect('home')

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        client_form = addClientForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            client_form = addClientForm(request.POST)
            if form.is_valid() and client_form.is_valid():
                user = form.save()
                client = client_form.save(commit=False)
                client.user = user
                client.save()
                username = form.cleaned_data.get('username')
                messages.success(request,"Cuenta creada para exitosamente para " + username)
                return redirect('login')

        context = {'form':form}
        return render(request,'register.html',context)

@login_required(login_url='login')
