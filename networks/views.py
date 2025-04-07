from django.shortcuts import render, redirect
from networks.models import UserData
from django.http import HttpResponse 
from django.contrib.auth import authenticate, login
from django.contrib import messages



def index (request):
    usuarios = UserData.objects.all()

      
    return render(request, 'networks/index.html', {'usuarios':usuarios})



def create_usuarios(request):
    usuarios = UserData.objects.all()
    if request.method == 'POST':
       
  
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

       
        UserData.objects.create(
            
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )
        return redirect('login_usuarios')

    return render (request, 'networks/create_user.html',{'usuarios':usuarios})



def login_usuarios(request):
    if request.method == 'POST':
     
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)  
            return redirect('index') 
        else:
            messages.error(request, 'erro de validação')
 
 
            return render(request, 'networks/login_user.html')
                              

    return render(request, 'networks/login_user.html')


     
     
     
    