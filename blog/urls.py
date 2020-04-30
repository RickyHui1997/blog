from django.contrib import admin
from django.urls import path
from webblog import views as v


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', v.signup),
    path('login/', v.user_login),
    path('user/', v.user),
    path('logout/', v.user_logout),
    path('', v.home)
]
