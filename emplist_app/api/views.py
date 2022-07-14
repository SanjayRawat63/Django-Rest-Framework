from re import T
import re
from emplist_app.api.serializers import EmployeeSerializer
from emplist_app.models import employees
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET','POST'])
def employees_list(request):
    if request.method == 'GET':
        emp_list=employees.objects.all()
        serializer=EmployeeSerializer(emp_list,many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer=EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
 
 
@api_view(['GET','PUT','DELETE'])
def employee_details(request,pk):
    if request.method == 'GET':
        emp_list=employees.objects.get(pk=pk)
        serializer=EmployeeSerializer(emp_list)
        return Response(serializer.data)
    
    if request.method=='PUT':
        emp_list=employees.objects.get(pk=pk)
        serializer=EmployeeSerializer(emp_list,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    
    if request.method=='DELETE':
        emp_list=employees.objects.get(pk=pk)
        emp_list.delete()
        return Response({"status":"This data is succesfully deleted"})
        