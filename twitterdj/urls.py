from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('me/',include('users.urls',namespace='users_app'))
]
