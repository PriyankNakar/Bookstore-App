from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from django.template import RequestContext

# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.tokens import PasswordResetTokenGenerator  
 

def login_view(request):
     return render(request,'users/Login.html')
def logout_view(request):
    logout(request)
    return redirect('Login')
def authenticates(request):
    if request.method == "POST":
        # Accessing email and password from form data
        username = request.POST["username-login"]
        password = request.POST["password-login"]

        # Check if email and password are correct, returning User object if so
        user = authenticate(request, username=username, password=password)

        # If user object is returned, log in and route to index page:
        if user:
            login(request, user)
            print(user)
            return  redirect('/home')
        # Otherwise, return login page again with new context
        else:
            if User.objects.filter(username=username).exists():
                return render(request, "users/Login.html", {
                    "message": "Invalid Password","li":True,'pass':True
                })
            else:
                return render(request, "users/Login.html", {
                    "message": "Invalid Username, User Doesn't Exist ","li":True,'pass':False
                })
    return render(request, "users/Login.html")
def createUser(request):
    if request.method == "POST":
        # Accessing email and password from form data
        username = request.POST["username-signup"]
        password = request.POST["password-signup"]
        password2 = request.POST["password2-signup"]
        if username!="":
            if  password2==password and password!="" and len(password)>7:
                if not User.objects.filter(username=username).exists():
                    User.objects.create_user(username=username,password=password)
                    return render(request,'users/signup.html',{"message":"Successfully Created Your Account","li":False,"name":username})
                else:
                    return render(request,'users/signup.html',{"message":"Username already exist","li":False,"username":True})
            elif password2!=password:
                 return render(request,'users/signup.html',{"message":"Type both passwords same","li":False,"username":False})
            else:
                 return render(request,'users/signup.html',{"message":"Your Password should not be blank or less than 7 ","li":False,"username":False})
        else:
             return render(request,'users/signup.html',{"message":"Username cannot be empty","li":False,"username":True})
    else:
        return render(request,'users/signup.html')
def profile(request):
    return redirect('/home')