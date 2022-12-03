from django.shortcuts import render, redirect
from .models import Player
from django.http import HttpResponse 
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        passwordAgain = request.POST['passwordAgain']
        

        if User.objects.filter(username=username).exists() or password != passwordAgain:
            error = "Alrady Taken"
            paswword_error = "Paswwords Don't Match"
            return render(request,'users/register.html',{'error':error,'paswword_error':paswword_error})
        else:
            # does this create a user or just a player? it seeems like it just creates a player
            user = User.objects.create_user(username=username,password=password)
            user.save()
            player = Player.objects.create(auth_user_link=user)
            player.save()
            print(player)
            
            return redirect('login')        
    
    return render(request,'users/register.html')

def login(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            auth_login(request, user)
            return redirect('/l')
        else:
            error = "bad username or password"
            return render(request,'users/login.html',{'error':error})

    return render(request,'users/login.html')

def logout(request):
    auth_logout(request) 
    return redirect('/login') 

def profile(request, user_id):
    user = User.objects.get(pk=user_id)
    context = {"player": Player.objects.get(auth_user_link=user)}
    return render(request,'users/details.html', context)
