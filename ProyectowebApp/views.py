from django.shortcuts import render, HttpResponse, redirect
from .forms import UserRegisterForm
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, "ProyectowebApp/home.html")


def contacto(request):
    return render(request, "ProyectowebApp/contacto.html")


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} ha sido creado')
            return redirect('Login')
    else:
        form = UserRegisterForm()
    context = {'form' : form}

    return render(request, "ProyectowebApp/register.html", context)
    
#class FormularioClienteView(HttpRequest):
