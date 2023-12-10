from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from .forms import ClientForm, SignUpForm, LoginForm
from .models import Client
from .models import User


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Form data is valid, process the data here
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # Hash the password before saving it to the database
            hashed_password = make_password(password)
            # Save the user to the database
            user = User.objects.create(name=name, email=email, password=hashed_password)
            user.save()
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def log_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                form.add_error(None, "Invalid email or password. Please try again.")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def index(request):
    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print(form.errors)
    clients = Client.objects.all()
    return render(request, 'index.html', {'form': form, 'clients': clients})


def my_form(request):
    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print(form.errors)
    return render(request, 'index.html', {'form': form})


def cv(request):
    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save()
            return render(request, 'cv.html', {'client': client})
        else:
            print(form.errors)
    return render(request, 'index.html', {'form': form})