from statistics import mode
from django.db import models

class Company(models.Model):
    title = models.CharField(max_length=50)
    address = models.CharField(max_length=50)


    def __str__(self) -> str:
        return self.title


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    working_date = models.DateField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    job = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.first_name

    