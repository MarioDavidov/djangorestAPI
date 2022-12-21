from django.db import models


class Companies(models.Model):
    company_name = models.CharField(max_length=20)
    logo = models.TextField(max_length=250)
    description = models.TextField(max_length=250)
