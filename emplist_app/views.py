from urllib import request
from django.http import JsonResponse
from django.shortcuts import render
from emplist_app.models import employees
from django.http import JsonResponse
# Create your views here.
def employee_list(request):
    emp_list=employees.objects.all()
    data={'employees':list(emp_list.values())}
    return JsonResponse(data)

def employee_details(request,pk):  
    emp_list=employees.objects.get(pk=pk)
    data={
        'name':emp_list.emp_name,
        'age':emp_list.emp_age,
        'designations':emp_list.emp_designation
    }
    return JsonResponse(data)