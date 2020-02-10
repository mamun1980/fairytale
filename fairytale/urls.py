from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html"), name="home"),
    path('accounts/login/',
         LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path('accounts/login/',
         LoginView.as_view(template_name="accounts/login.html"), name="register"),
    path('admin/', admin.site.urls),
]
