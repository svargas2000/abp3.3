from django.urls import path
from ProyectowebApp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('home', views.home, name="Home"),
    path('contacto', views.contacto, name="Contacto"),
    path('register', views.register, name="Register"),
    path('login', LoginView.as_view(template_name="ProyectowebApp/login.html"), name="Login"),
    path('logout', LogoutView.as_view(template_name="ProyectowebApp/logout.html"), name="Logout"),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)