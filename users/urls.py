from django.urls import path, include
from . import views as users_views  

app_name = 'users'

urlpatterns = [
	path('register/',users_views.RegisterView,name='register'),
	path('login/',users_views.LoginView,name='profile')
]