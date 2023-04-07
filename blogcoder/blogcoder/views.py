from django.http import HttpResponse
from django.template import Template, Context

def inicio(request):
    
    miHtml = open("C:/Users/Bruno/Desktop/PROYECTO_BLOG/blogcoder/blogcoder/plantillas/inicio.html")

    plantilla = Template(miHtml.read())

    miHtml.close()

    miContexto = Context()

    documento = plantilla.render(miContexto)

    return HttpResponse(documento)

def about(request):
    
    miHtml = open("C:/Users/Bruno/Desktop/PROYECTO_BLOG/blogcoder/blogcoder/plantillas/about.html")

    plantilla = Template(miHtml.read())

    miHtml.close()

    miContexto = Context()

    documento = plantilla.render(miContexto)

    return HttpResponse(documento)
    