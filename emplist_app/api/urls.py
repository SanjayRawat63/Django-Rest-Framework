
from django.contrib import admin
from django.urls import path
from emplist_app.api.views import EmployeeDetails,EmployeesList
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('emplist/', EmployeesList.as_view(), name="emp-list"),
    path('<int:pk>/', EmployeeDetails.as_view(), name="emp-details"),
    # path('login/', obtain_auth_token, name='login'),
    # path('register/', registration_view, name='register'),
    # path('logout/', logout_view, name='logout'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
