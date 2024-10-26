from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

#je restrain l'acces au utilsateur non connecté
@login_required
def home(request):
    return render(request, 'blog/home.html')