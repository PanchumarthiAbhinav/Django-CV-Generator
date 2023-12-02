from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from .forms import ClientForm
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
            user = User(name=name, email=email, password=hashed_password)
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
   client = ClientForm()
   name = request.POST.get("y_name")
   pos = request.POST.get("position")
   prf = request.POST.get("profile")
   loc = request.POST.get("location")
   mail = request.POST.get("email")
   num = request.POST.get("phone_number")
   ln = request.POST.get("linkedin")
   exp = request.POST.get("experience")
   eud = request.POST.get("education")
   lan = request.POST.get("languages")
   skl = request.POST.get("skills")
   certifi = request.POST.get("certificate")

   data = {
       'form': client,
       'y_name': name,
       'pos':pos, 
       'prf':prf,
       'loc':loc, 
       'mail':mail, 
       'num':num, 
       'ln':ln,
       'exp':exp,
       'eud':eud,
       'lan':lan,
       'skl':skl,
       'certifi':certifi
   }
   return render(request, "index.html", data)



def my_form(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors) 
    else:
        form = ClientForm()

    return render(request, 'index.html', {'form': form})



def cv(request) :
    if request.method =='POST':
        name = request.POST["y_name"]
        pos = request.POST["position"]
        prf = request.POST["profile"]
        loc = request.POST["location"]
        mail = request.POST["email"]
        num = request.POST["phone_number"]
        ln = request.POST["linkedin"]
        exp = request.POST["experience"]
        eud = request.POST["education"]
        lan = request.POST["languages"]
        skl = request.POST["skills"]
        certifi = request.POST["certificate"]
        extracurricular = request.POST.get("extracurricular")

        dict = {
            'y_name' : name,
            'pos':pos, 
            'prf':prf,
            'loc':loc, 
            'mail':mail, 
            'num':num, 
            'ln':ln,
            'exp':exp,
            'eud':eud,
            'lan':lan,
            'skl':skl,
            'certifi':certifi,
            'extracurricular': extracurricular
        }
        return render(request,'cv.html',dict);






