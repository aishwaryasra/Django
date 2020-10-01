from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.HomeView.as_view()),
]

from django.conf import settings
try: 
    if len(settings.SOCIAL_AUTH_GITHUB_KEY) > 0 :
        social_login = 'registration/login_social.html'
        urlpatterns += [
            path('accounts/login/', auth_views.LoginView.as_view(template_name=social_login)),
        ]
        print('Using',social_login,'as the login template')
except:
    print('Using registration/login.html as the login template')