from os import stat_result
from re import T
import re
from emplist_app.api.serializers import EmployeeSerializer,RegistrationSerializer
from emplist_app.models import employees
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

class EmployeesList(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
         emp_list = employees.objects.all()
         serializer=EmployeeSerializer(emp_list,many=True)
         return Response(serializer.data)
     
    def post(self,request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
         
class EmployeeDetails(APIView):
   
    def get(self,request,pk):
        try:
            emp_list = employees.objects.get(pk=pk)
        except employees.DoesNotExist:
             return Response({"Error":"Employee Details Not Found"},status=status.HTTP_404_NOT_FOUND)
        serializer=EmployeeSerializer(emp_list)
        return Response(serializer.data)
    
    def put(self,request,pk):
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
        
    def delete(self,request,pk):
        emp_list=employees.objects.get(pk=pk)
        emp_list.delete()
        return Response({"msg": "Employee Details successfully deleted"}, status=status.HTTP_204_NO_CONTENT)
 
 
# @api_view(['POST'])
# def logout_view(request):

#     if request.method == 'POST':
#         request.user.auth_token.delete()
#         return Response(status=status.HTTP_200_OK)


# @api_view(['POST'])
# def registration_view(request):

#     if request.method == 'POST':
#         serializer = RegistrationSerializer(data=request.data)
        
#         data = {}
        
#         if serializer.is_valid():
#             account = serializer.save()
            
#             data['response'] = "Registration Successful!"
#             data['username'] = account.username
#             data['email'] = account.email
#             refresh = RefreshToken.for_user(account)
#             data['token'] = {
#                                  'refresh': str(refresh),
#                                  'access': str(refresh.access_token),
#                              }
       
#         else:
#             data = serializer.errors
        
#         return Response(data, status=status.HTTP_201_CREATED)