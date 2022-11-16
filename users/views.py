from django.shortcuts import render, redirect
from .models import Player
from django.http import HttpResponse 

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        passwordAgain = request.POST['passwordAgain']
        

        if Player.objects.filter(username=username).exists() or password != passwordAgain:
            error = "Alrady Taken"
            paswword_error = "Paswwords Don't Match"
            return render(request,'users/register.html',{'error':error,'paswword_error':paswword_error})
        else:

            user = Player.objects.create_user(username,password)
            user.save()
            return redirect('login')        
    
    return render(request,'users/register.html')

def login(requst):
    return HttpResponse(f'login')

def profile(requst, player_id):
    return HttpResponse(f'looking up player {player_id}')
