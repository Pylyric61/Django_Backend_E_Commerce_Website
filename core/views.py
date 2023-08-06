from django.shortcuts import render, redirect
from item.models import Category, Item
from .forms import SignupForm
from django.contrib import messages, auth
from django.contrib.auth import authenticate


def index(request):
    items = Item.objects.filter(is_sold=False)[:6]
    categories = Category.objects.all()
    return render(request,'core/index.html', {'categories':categories, 'items':items})

def contact(request):
    return render(request,'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
        else:
            if len(request.POST['password1']) < 8 and len(request.POST['password2']) < 8:
                messages.info(request, "Password must contain at least 8 characters") 
                return render(request, 'core/signup.html', {'form':form})
            return render(request,'core/signup.html', {'form':form})


    else:
        form = SignupForm()
    return render(request,'core/signup.html', {'form':form})

def logout(request):
    auth.logout(request)
    return redirect('/')