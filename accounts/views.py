from django.shortcuts import render, redirect
from django.http import HttpResponse

from accounts.decorators import unauthenticated_user
from .models import *
from .forms import *
from .filter import AnimeFilter, AnimeInfoFilter

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from .decorators import unauthenticated_user, allowed_users, admin_only

# Create your views here.

# HOME PAGE
def home(request):
    return render(request, 'accounts/home.html')

# SEARCH PAGE
@login_required(login_url='signin')
def searchPage(request):
    animeinfos = AnimeInfo.objects.all()

    #FOR FILTERS ( SEARCH FUNCTION )
    myFilter = AnimeInfoFilter(request.GET, queryset=animeinfos)
    animeinfos = myFilter.qs
    
    return render(request, 'accounts/searchpage.html', {'animeinfos': animeinfos, 'myFilter': myFilter})

# MAIN HOME PAGE
@login_required(login_url='signin')
def homePage(request):
    animeinfos = AnimeInfo.objects.all()
    return render(request, 'accounts/home-content.html', {'anime': animeinfos})

# SETTINGS SECTION
@login_required(login_url='signin')
def setting(request):
    settings = Setting.objects.all()
    return render(request, 'accounts/settings.html', {'settings': settings})

# CLICKED ANIME PAGE
@login_required(login_url='signin')
def lorem(request, pk_test):
    anime = AnimeInfo.objects.get(id=pk_test)
    context = {'anime':anime}
    return render(request, 'accounts/demon-slayer.html', context)

# SIGN UP PAGE
@unauthenticated_user
def signup(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'Account was created for ' + username)

            return redirect('signin')

    context = {'form': form}
    return render(request, 'accounts/signup.html', context)

# SIGN IN SECTION
@unauthenticated_user
def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')
    
    context = {}
    return render(request, 'accounts/signin.html', context)

# SIGN OUT SECTION
def signout(request):
    logout(request)
    return redirect('signin')

# USER PAGE
@login_required(login_url='signin')
@allowed_users(allowed_roles=['customer'])
def userPage(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'accounts/user.html', context)

# ADMIN DASHBOARD PAGE
@login_required(login_url='signin')
@allowed_users(allowed_roles=['admin'])
# @admin_only
def dashboard(request):
    animeinfos = AnimeInfo.objects.all()
    customers = Customer.objects.all()

    #TOTAL CUSTOMER
    total_customers = customers.count()

    #TOTAL ANIMES
    total_animes = animeinfos.count()

    #FOR FILTERS ( SEARCH FUNCTION )
    myFilter = AnimeFilter(request.GET, queryset=animeinfos)
    animeinfos = myFilter.qs

    context = {'anime': animeinfos, 'customers': customers, 'total_customers': total_customers, 'total_animes': total_animes, 'myFilter': myFilter}
    return render(request, 'accounts/dashboard.html', context)

# ADMIN CREATE ANIME PAGE
@login_required(login_url='signin')
@allowed_users(allowed_roles=['admin'])
def createanime(request):
    form = AnimeInfoForm()
    if request.method == 'POST':
        form = AnimeInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dashboard')

    context = {'form': form}
    return render(request, 'accounts/createanime.html', context)

# ADMIN UPDATE ANIME PAGE
@login_required(login_url='signin')
@allowed_users(allowed_roles=['admin'])
def updateanime(request, pk):
    anime = AnimeInfo.objects.get(id=pk)
    form = AnimeInfoForm(instance=anime)
    if request.method == 'POST':
        form = AnimeInfoForm(request.POST, instance=anime)
        if form.is_valid():
            form.save()
            return redirect('/dashboard')

    context = {'form': form}
    return render(request, 'accounts/createanime.html', context)

# ADMIN DELETE ANIME PAGE
@login_required(login_url='signin')
@allowed_users(allowed_roles=['admin'])
def deleteanime(request, pk):
    anime = AnimeInfo.objects.get(id=pk)
    if request.method == "POST":
        anime.delete()
        return redirect('/dashboard')
        
    context = {'anime': anime}
    return render(request, 'accounts/deleteanime.html', context)

# TERMS AND POLICY SECTION
def terms(request):
    context = {}
    return render(request, 'accounts/terms.html', context)