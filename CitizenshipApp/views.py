from django.shortcuts import render
from .forms import UserSignupForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'home.html')

def signupuser(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Signed-up Succesfully')
            return HttpResponseRedirect('/')
    else:
        form = UserSignupForm()
        return render(request,'signupuser.html',{'form':form})

def loginuser(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                user = form.cleaned_data['username']
                pwd = form.cleaned_data['password']
                user = authenticate(request, username=user,password=pwd)
                if user is not None:
                    login(request, user)
                    messages.success(request,'Logged In succesfully')
                    return HttpResponseRedirect('/userprofile/')

        else:
            form = AuthenticationForm()
            return render(request,'loginuser.html',{'form':form})
    else:
        return HttpResponseRedirect('/userprofile/')

def userprofile(request):
    return render(request,'userprofile.html')

def logoutuser(request):
    logout(request)
    return HttpResponseRedirect('/')