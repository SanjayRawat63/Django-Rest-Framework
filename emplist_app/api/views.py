from os import stat_result
from re import T
import re
from emplist_app.api.serializers import EmployeeSerializer
from emplist_app.models import employees
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
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
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
 
 
@api_view(['GET','PUT','DELETE'])
def employee_details(request,pk):
    
    if request.method == 'GET':
        try:
            emp_list=employees.objects.get(pk=pk)
        except employees.DoesNotExist:
             return Response({"Error":"Employee Details Not Found"},status=status.HTTP_404_NOT_FOUND)
        serializer=EmployeeSerializer(emp_list)
        return Response(serializer.data)
    
    if request.method=='PUT':
        try:
            emp_list = employees.objects.get(pk=pk)
        except employees.DoesNotExist:
            return Response({"Error": "Employee Details Not Found"}, status=status.HTTP_404_NOT_FOUND)
        serializer=EmployeeSerializer(emp_list,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    
    if request.method=='DELETE':
        emp_list=employees.objects.get(pk=pk)
        emp_list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        