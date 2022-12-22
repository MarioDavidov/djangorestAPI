from django.db import models
# from companies_api.validators import salary


class Companies(models.Model):
    company_name = models.CharField(max_length=20)
    logo = models.ImageField(upload_to='companies_logos', null=True, max_length=255)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.company_name


class Employee(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    photo = models.ImageField(upload_to='employee_picture', null=True, max_length=255)
    position = models.CharField(max_length=20)
    salary = models.PositiveIntegerField()
    employee_company = models.ForeignKey(Companies, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name
