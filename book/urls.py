
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.overview,name='api_overview'),
    path('list-books',views.listBook,name='listBook'),
    path('author/add',views.add,name='add'),
    path('user/search/<str:pk>',views.search,name='search'),
    path('user/upvote/<str:pk>',views.upvote,name='upvote'),
    path('user/comment/<str:pk>',views.comment,name='comment')
]
