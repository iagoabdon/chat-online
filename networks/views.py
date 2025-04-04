from django.shortcuts import render, redirect
from networks.models import UserData
from django.http import HttpResponse 
from django.contrib.auth.models import User



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

    return render (request, 'networks/create_user.html',{'usuarios':usuarios})
