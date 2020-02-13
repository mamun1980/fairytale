from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html"), name="home"),
    
    path('accounts/login/', LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path('accounts/register/', TemplateView.as_view(template_name="accounts/register.html"), name="register"),
    path('accounts/profile/', TemplateView.as_view(template_name="accounts/profile.html"), name="profile"),
    path('accounts/logout/', LogoutView.as_view(next_page='/'), name="logout"),

    path('accounts/password_reset/', TemplateView.as_view(template_name="accounts/register.html"), name="password_reset"),
    path('accounts/password_reset/done/', TemplateView.as_view(template_name="accounts/register.html"), name="password_reset_done"),
    path('accounts/password_change/', TemplateView.as_view(template_name="accounts/register.html"), name="password_change"),
    path('accounts/password_change/done/', TemplateView.as_view(template_name="accounts/register.html"), name="password_change_done"),
    path('accounts/reset/<uidb64>/<token>/', TemplateView.as_view(template_name="accounts/register.html"), name="password_reset_confirm"),
    path('accounts/reset/done/', TemplateView.as_view(template_name="accounts/register.html"), name="password_reset_complete"),


    path('admin/', admin.site.urls),
]
