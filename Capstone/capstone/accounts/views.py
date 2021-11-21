from django.contrib import messages, auth
from django.shortcuts import render, redirect

from pages.models import User

# Create your views here.
def login(request):
    if request.method == 'POST':
        #Register User
        return
    else:
        return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
    #Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        question1 = request.POST['question1']
        question2 = request.POST['question2']
        question3 = request.POST['question3']
        
        #Check to see if passwords match
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'The username is taken.')
                return redirect('register')
            else:
                user = User.objects.create(first_name=first_name,last_name=last_name,username=username,password=password,password2=password2,question1=question1,question2=question2,question3=question3)
                # auth.login(request, user)
                messages.success(request, 'You are now logged in.')
                return redirect('/')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def logout(request):
    return redirect(request, 'index')