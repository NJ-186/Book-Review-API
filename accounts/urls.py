
from django.urls import path,include
from . import views
from .views import AuthorRegistration, NormalUserRegistration, UserLogin

urlpatterns = [
    path('',views.overview,name='overview'),
    path('register/author',AuthorRegistration.post),
    path('register/user',NormalUserRegistration.post),
    path('login',UserLogin.post),
]
