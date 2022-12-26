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
    company_post_pk = reverse('company details api', args=[4])

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
        self.client.post(self.companies_url, data, format="json")

        edited_company = {
            "company_name": "Edited",

            "description": "Edited Description",
        }
        response = self.client.post(self.company_url_post_pk, edited_company, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['company_name'], 'Edited')

    # def test_delete_company(self):
    #     delete = self.client.delete(self.company_post_pk)
    #     self.assertEqual(delete.status_code, status.HTTP_200_OK)


# ///               EMPLOYEE TEST STARTS FROM HERE                   ///

class EmployeeListApiViewTest(APITestCase):
    employees_url = reverse('employee list api')
    companies_url = reverse('company list api')
    employee_url_post_pk = reverse('employee details api', args=[1])
    rename_me = reverse('employee details api', args=[2])
    def test_get_employees(self):
        response = self.client.get(self.employees_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_employee(self):
        company_for_employe = {
            "company_name": "Company for Employee",
            "description": "Description",
        }
        c =self.client.post(self.companies_url, company_for_employe, format="json")
        print(c.data["id"])
        data = {
            "first_name": "Batman",
            "last_name": "Batsy",
            "date_of_birth": "2022-12-22",

            "position": "Hero",
            "salary": 1000,
            "employee_company": 6,
        }
        response = self.client.post(self.employees_url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["first_name"], "Batman")



class EmployeeDetailApiViewTest(APITestCase):
    companies_url = reverse('company list api')
    employees_url = reverse('employee list api')
    employee_url = reverse('employee details api', args=[1])
    employee_ti_edit_with_pk = reverse('employee details api', args=[2])
    employee_url_pk = reverse('employee details api', args=[6])

    def test_get_employee(self):
        company_for_em = {
            "company_name": "Working station",
            "description": "alabala",
        }
        compani = self.client.post(self.companies_url, company_for_em, format="json")
        self.assertEqual(compani.status_code, status.HTTP_201_CREATED)
        # print(compani.data["id"])
        data_employee = {
            "first_name": "Robin",
            "last_name": "Hero",
            "date_of_birth": "2012-12-22",

            "position": "SuperHero",
            "salary": 1,
            "employee_company": 4,
        }
        emplo = self.client.post(self.employees_url, data_employee, format="json")
        self.assertEqual(emplo.status_code, status.HTTP_201_CREATED)
        # print(emplo.data["id"])
        # 1
        employee = self.client.get(self.employee_url)
        self.assertEqual(employee.status_code, status.HTTP_200_OK)
        self.assertEqual(employee.data['first_name'], 'Robin')

    def test_post_employee_with_pk(self):
        company_for_em_with_pk = {
            "company_name": "for employee with pk",
            "description": "close enough",
        }
        compani = self.client.post(self.companies_url, company_for_em_with_pk, format="json")

        employee = {
            "first_name": "Michael",
            "last_name": "Bensom",
            "date_of_birth": "2022-12-22",
            "position": "Manager",
            "salary": 9999,
            "employee_company": 5,
        }
        response = self.client.post(self.employees_url, employee, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        employee_edited = {
            "first_name": "Edited",
            "last_name": "One",
            "date_of_birth": "2022-12-22",
            "position": "no more manager",
            "salary": 1500,
            "employee_company": 5,
        }
        response_edited_employee = self.client.post(self.employee_ti_edit_with_pk, employee_edited, format="json")
        self.assertEqual(response_edited_employee.status_code, status.HTTP_200_OK)
        self.assertEqual(response_edited_employee.data['first_name'], 'Edited')
    #
    # def test_delete_employee(self):
    #     response = self.client.delete(self.employee_url_pk)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
