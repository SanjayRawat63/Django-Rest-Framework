from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class employees(models.Model):
   
    emp_name=models.CharField(max_length=100)
    emp_age=models.PositiveIntegerField()
    emp_designation=models.CharField(max_length=100)
    dummy_user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.emp_name
    