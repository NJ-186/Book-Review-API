
from django.urls import path,include
from .views import AuthorRegistration, NormalUserRegistration, UserLogin, overview

urlpatterns = [
    path('',overview,name='overview'),
    path('register/author',AuthorRegistration.post),
    path('register/user',NormalUserRegistration.post),
    path('login',UserLogin.post),
]
