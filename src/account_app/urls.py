from django.urls import path
from .views import *
from django.urls import path
from .views import ChangePasswordView

urlpatterns = [
    
]
app_name = "account_app"

urlpatterns = [
    path("signup/", signup_view, name="signup"),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),
    path("dashboard/", dashboard_view, name="dashboard"),

]