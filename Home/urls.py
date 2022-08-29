from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('/companies', views.companies, name='companies'),
    path('/companies/<int:id>', views.companies_detail, name="companies-detail"),
    path('/companies-list', views.companies_list, name='companies_list'),
]
