from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='index'),
    path('me', views.me, kwargs={'full_name': 'Олимской В.В.', 'age': 21, 'hobby': 'Django'}, name='me'),
    path('about', views.about, kwargs={'sity': 'Набережные Челны'}, name='about'),
    path('contact',views.my_contact, kwargs={'contact': "https://github.com/olimech/Django.git", 'telegram': '9534128890'})
]