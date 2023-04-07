from django.urls import path
from accounts.views import inicioAccounts, login_request
from accounts import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", inicioAccounts, name="InicioAccounts"),
    path("login", views.login_request, name = "Login"),
    path("register", views.register, name = "Register"),
    path("logout", LogoutView.as_view(template_name= "accounts/logout.html"), name = "Logout")
    

]