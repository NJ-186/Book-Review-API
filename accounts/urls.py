
from django.urls import path,include
from . import views
from .views import AuthorRegistration, NormalUserRegistration, UserLogin

urlpatterns = [
    path('',views.overview,name='overview'),
    path('register/author',AuthorRegistration.as_view()),
    path('register/user',NormalUserRegistration.as_view()),
    path('login',UserLogin.as_view()),
]
