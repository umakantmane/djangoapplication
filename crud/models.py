from django.db import models

# Create your models here.


class Employee(models.Model):

    emp_name = models.CharField(max_length=50)
    emp_email = models.EmailField(unique=True)
    emp_address = models.CharField(max_length=250)

    def __str__(self):

        return self.emp_email

    class Meta:

        db_table = 'emp'

class EmployeeProfile(models.Model):

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    age = models.CharField(max_length=11)
    city = models.CharField(max_length=50)
    pincode = models.CharField(max_length=10)

    class Meta:
        db_table = 'emp_profile'


class EmployeeEducation(models.Model):

    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    edu_name = models.CharField(max_length=50)
    edu_uni = models.CharField(max_length=100)

    class Meta:

        db_table = 'emp_education'
