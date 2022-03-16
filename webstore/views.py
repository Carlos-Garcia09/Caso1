from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.db.models import Count

# Create your views here.

@login_required(login_url='guest')
def home(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request,'home.html',context)

def guest(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request,'guest.html',context)

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

@login_required(login_url='login')
def apanel(request):
    if request.user.is_staff:
        if request.user.is_superuser:
            role = "Superusuario"
            products = Product.objects.all()
        else:
            role = Client.objects.get(user=User.objects.get(pk=request.user.id)).publisher
            products = Product.objects.filter(publisher=role)
        context = {
            'role':role,
            'products':products,
        }
        return render(request,'apanel.html',context)
    else:
        return redirect('home')
    
    @login_required(login_url='login')
def product_page(request,pk):
    product = Product.objects.get(pk=int(request.path.split('/')[2]))
    sug = Product.objects.filter(genre=product.genre).exclude(pk=pk)
    context = {
        'product':product,
        'sug':sug,
        'flag':len(sug)
    }
    return render(request,'product.html',context)
