
from django.contrib import admin
from django.urls import path
from emplist_app.api.views import EmployeeDetails,EmployeesList
urlpatterns = [
    path('emplist/', EmployeesList.as_view(), name="emp-list"),
    path('<int:pk>/', EmployeeDetails.as_view(), name="emp-details"),

]
