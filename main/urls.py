"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from finecap.views import reserva_criar, index, reserva_listar, reserva_remover, reserva_detalhar
from User.views import login_view as login, logout_view, create_user
from django.conf.urls.static import static 
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = 'index'),
    path('reserva/criar/', reserva_criar, name = 'reserva_criar'),
    path('reserva/remover/<int:id>/', reserva_remover, name = 'reserva_remover'),
    path('reserva/listar/', reserva_listar, name = 'reserva_listar'),
    path('reserva/<int:id>/', reserva_detalhar, name = 'reserva_detalhar'),
    path('login/', login, name='login'),
    path('logout/', logout_view, name='logout'),
    path('create_user/', create_user, name='create_user')
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
