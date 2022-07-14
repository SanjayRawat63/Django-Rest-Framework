from django.db import models

# Create your models here.
class employees(models.Model):
    emp_name=models.CharField(max_length=100)
    emp_age=models.PositiveIntegerField()
    emp_designation=models.CharField(max_length=100)
    
    def __str__(self):
        return self.emp_name
    