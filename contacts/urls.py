from django.contrib import admin
from django.urls import path
from . import views

app_name = 'contacts'

urlpatterns = [
    path('contacts/', views.contacts_list, name='contacts_list'),
    path('contacts/create/', views.create_contact, name='create_contact'),
]