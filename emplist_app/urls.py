 
from django.contrib import admin
from django.urls import path
from emplist_app.views import employee_details, employee_list
urlpatterns = [
    path('emplist/',employee_list,name="emp-list"),
    path('<int:pk>',employee_details,name="emp-details")
]
