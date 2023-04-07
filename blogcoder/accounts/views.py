from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def inicioAccounts(request):

    miHtml = open("C:/Users/Bruno/Desktop/PROYECTO_BLOG/blogcoder/accounts/templates/accounts/inicioAccounts.html")

    plantilla = Template(miHtml.read())

    miHtml.close()

    miContexto = Context()

    documento = plantilla.render(miContexto)

    return HttpResponse(documento)

def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid:
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)

                return render(request, "accounts/inicioAccounts.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "accounts/inicioAccounts.html", {"mensaje":"Error, datos incorrectos"})
        else:
            return render(request, "accounts/inicioAccounts.html", {"mensaje":"Error, formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "accounts/inicioAccounts.html", {"form":form})


def register(request):

    if request.method == "POST":
        
        form = UserCreationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request, "accounts/inicioAccounts.html", {"mensaje":"Usuario creado!"})
    
    else:
        form = UserCreationForm()

    return render(request, "accounts/registro.html" , {"form":form})
