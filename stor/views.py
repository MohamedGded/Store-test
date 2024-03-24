from django.shortcuts import render,redirect
from .models import Product,Category
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms



def category(request,foo):
      foo=foo.replace('-','')
      try:
       category=Category.objects.get(name=foo)
       products=Product.objects.filter(category=category)
       return redirect(category,'category.html',{'products':products,'category':category})
      except:
         messages.success(request,('category**********!'))
         return redirect('home')

def product(request,pk):
      product=Product.objects.get(id=pk)
      return render(request,'product.html',{'product':product})



def home(request):
    products=Product.objects.all()
    return render(request,'home.html',{'products':products})

def about(request):
    return render(request,'about.html',{})

def login_user(request):
    if request.method=='POST':
       username=request.POST['username']
       password=request.POST['password']
       user=authenticate(request,username=username,password=password)
       if user is not None:
           login(request,user)
           messages.success(request,('you have..............!'))
           return redirect('home')
       else:
            messages.success(request,('Erorrrr'))
            return redirect('login')
    else:
        return render(request,'login.html',{})

def logout_user(request):
    logout(request)
    messages.success(request,('logouuuuut**********!'))
    return redirect('home')
"""
def register_user(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid:
            form.save()
            username=form.cleaned_data['username']
            passwoed=form.cleaned_data['passwoed1']

            user=authenticate(username=username,passwoed=passwoed)
            login(request,user)
            messages.success(request,('Successflly!!!'))
            return redirect('home')
        else:
            messages.success(request,('No regstier...'))
            return redirect('register')
    else:
        return render(request,'register.html',{'form':form})"""

def register_user(request):
	form = SignUpForm()
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			# first_name = form.cleaned_data['first_name']
			# second_name = form.cleaned_data['second_name']
			# email = form.cleaned_data['email']
			# Log in user
			user = authenticate(username=username, password=password)
			login(request,user)
			messages.success(request, ("You have successfully registered! Welcome!"))
			return redirect('home')
	
	return render(request, "register.html", {'form':form})