from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from . import forms

# Create your views here.


#vue de l'authentification
def login_user(request):

    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.method)
        if form.is_valid():
            user =(
                authenticate(
                    username = form.cleanned_data['username'],

                    password = form.cleanned_data['password'],
                )
            )
            if user is not None :

                login(request, user)
                return redirect('home')
    
            message = 'identifiant non reconue'
    return render(request, 'authentication/login.html', context={'message':message, 'form':form})


#vue de la deconnexion
def logout_user(request):

    logout(request)
    redirect('login')