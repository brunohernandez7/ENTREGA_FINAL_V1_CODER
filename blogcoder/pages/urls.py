from django.urls import path
from pages.views import inicioPages, crearBlog, verPaginas

urlpatterns = [
    path("", inicioPages, name="InicioPages"),
    path("crearBlog/", crearBlog, name="CrearBlog"),
    path("verPaginas/", verPaginas, name="VerPaginas"),
]