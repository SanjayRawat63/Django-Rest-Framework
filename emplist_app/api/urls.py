
from django.contrib import admin
from django.urls import path
from emplist_app.api.views import employee_details, employees_list
urlpatterns = [
    path('emplist/', employees_list, name="emp-list"),
    path('<int:pk>/', employee_details, name="emp-details")
]
