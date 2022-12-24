from rest_framework.test import APITestCase, APIClient
# from companies_api.models import Companies, Employee
from django.urls import reverse, resolve
# from companies_api.views import CompanyListApiView
from rest_framework import status


class CompaniesApiViewTest(APITestCase):
    companies_url = reverse('company list api')
    company_url = reverse('company details api', args=[1])
    company_url_post_pk = reverse('company details api', args=[3])
    company_url_for_delete = reverse('company details api', args=[2])

    def test_get_companies(self):
        response = self.client.get(self.companies_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_company(self):
        data = {
            "company_name": "Fake Company",
            "description": "Short Description",
        }
        response = self.client.post(self.companies_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["company_name"], "Fake Company")

    def test_get_company(self):
        data = {
            "company_name": "Company for Edit",
            "description": "Description for Edit",
        }
        self.client.post(self.companies_url, data, format="json")
        company = self.client.get(self.company_url)
        self.assertEqual(company.status_code, status.HTTP_200_OK)
        self.assertEqual(company.data['company_name'], 'Company for Edit')

    def test_post_company_with_pk(self):
        data = {
            "company_name": "Company 3",

            "description": "Short",
        }
        response_2 = self.client.post(self.companies_url, data, format="json")
        print(response_2.data["id"])
        edited_company = {
            "company_name": "Edited",

            "description": "Edited Description",
        }
        response = self.client.post(self.company_url_post_pk, edited_company, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['company_name'], 'Edited')

    def test_delete_company(self):
        delete = self.client.delete(self.company_url)
        self.assertEqual(delete.status_code, status.HTTP_200_OK)



# ///               EMPLOYEE TEST STARTS FROM HERE                   ///

class EmployeeListApiViewTest(APITestCase):
    employees_url = reverse('employee list api')
    companies_url = reverse('company list api')
    employee_url_post_pk = reverse('employee details api', args=[1])

    def test_get_employees(self):
        response = self.client.get(self.employees_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_employee(self):
        company_for_employe = {
            "company_name": "Company for Employee",
            "description": "Description",
        }
        company = self.client.post(self.companies_url, company_for_employe, format="json")
        print(company.data["id"])
        data = {
            "first_name": "Batman",
            "last_name": "Batsy",
            "date_of_birth": "2022-12-22",

            "position": "Hero",
            "salary": 1000,
            "employee_company": 7,
        }
        response = self.client.post(self.employees_url, data, format="json")
        print(response.data["id"])
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["first_name"], "Batman")


class EmployeeDetailApiViewTest(APITestCase):
    companies_url = reverse('company list api')
    employees_url = reverse('employee list api')
    employee_url = reverse('employee details api', args=[1])

    def setUp(self):
        data_company = {
            "company_name": "Fake Company",
            "description": "Short Description",
        }
        self.client.post(self.companies_url, data_company, format="json")
        data_employee = {
            "first_name": "John",
            "last_name": "Doe",
            "date_of_birth": "2022-12-22",

            "position": "Manager",
            "salary": 100,
            "employee_company": 1,
        }
        self.client.post(self.employees_url, data_employee, format="json")

    def test_get_employee(self):
        employee = self.client.get(self.employee_url)
        self.assertEqual(employee.status_code, status.HTTP_200_OK)
        self.assertEqual(employee.data['first_name'], 'John')

    def test_post_company_with_pk(self):
        edited_employee = {
            "first_name": "Michael",
            "last_name": "Bensom",
            "date_of_birth": "2022-12-22",
            "position": "Manager",
            "salary": 9999,
            "employee_company": 1,
        }
        response = self.client.post(self.employee_url, edited_employee, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['salary'], 9999)

    def test_delete_employee(self):
        response = self.client.delete(self.employee_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
