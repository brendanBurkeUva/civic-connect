from django.urls import path

from . import views

app_name = 'civic'
urlpatterns = [
    path('', views.index, name='index'),
    path('submit/', views.submit, name='submit'),
    path('search/', views.search, name='search'),
    path('rep/', views.rep, name='rep'),
    path('resources/', views.resources, name="resources"),
    path('user/', views.userpage, name="userpage"),
    path('find/', views.find, name="find"),
]
