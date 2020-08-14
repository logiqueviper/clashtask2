from django.shortcuts import render,redirect
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def signup(request):
    if request.method == 'POST':
        data = request.POST
        uname = data['uname']
        fname = data['fname']
        lname = data['lname']
        email = data['email']
        phno = data['phno']
        pd = data['pd']
        cpd = data['cpd']
        if pd == cpd:
            try:
                user = User.objects.get(username = uname)
                return render(request,'users/signup.html',{'message':"User already exists"})
            except:
                user = User.objects.create_user(username = uname,password = pd,first_name =fname,last_name = lname,email =email)
                user.save()
                profile = UserProfile(user = user,phno = phno)
                profile.save()
                return render(request,'users/signup.html',{ 'message': "User has been successfully created !"})
                
        return render(request,'users/signup.html',{'message':"passwords do not match try again!"})
    return render(request,'users/signup.html')
def log_in(request):
    if request.method =="POST":
        uname = request.POST['uname']
        pd = request.POST['pd']
        user = authenticate(username = uname,password = pd)
        if user is None:
            return render(request,'users/login.html',{'message':"invalid username or password try again"})
        return  redirect('success')
    return render(request,'users/login.html')
def success(request):
    return render(request,'users/success.html')
def log_out(request):
    logout(request)
    return render(request,'users/logout.html')
        
