from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from pages.forms import BlogFormulario
from .models import Blog
# Create your views here.

def inicioPages(request):
    
    miHtml = open("C:/Users/Bruno/Desktop/PROYECTO_BLOG/blogcoder/pages/templates/pages/inicioPages.html")

    plantilla = Template(miHtml.read())

    miHtml.close()

    miContexto = Context()

    documento = plantilla.render(miContexto)

    return HttpResponse(documento)

def verPaginas(request):

    blogs = Blog.objects.all()
    contexto = {"blogs":blogs}

    return render(request, "pages/verPaginas.html", contexto)


def crearBlog(request):

    if request.method == "POST":

        miFormulario = BlogFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data
            blog = Blog(titulo=informacion["titulo"], resumen=informacion["resumen"], texto=informacion["texto"])
            blog.save()

            return render(request, "pages/crearBlog.html")
    
    else:
        miFormulario = BlogFormulario()
    
    return render(request, "pages/crearBlog.html", {"miFormulario":miFormulario})

