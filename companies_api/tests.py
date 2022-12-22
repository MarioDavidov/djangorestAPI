from rest_framework.test import APITestCase
from companies_api.models import Companies, Employee
from django.urls import reverse, resolve
from companies_api.views import CompanyListApiView
from rest_framework import status


class CompaniesApiViewTest(APITestCase):
    companies_url = reverse('company list api')

    def test_get_companies(self):
        response = self.client.get(self.companies_url)
        # testvame dali vlizame v lista s kompaniite
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_company(self):
        data = {
            "company_name": "Fake Company",
            "description": "Short Description",
        }
        response = self.client.post(self.companies_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["company_name"], "Fake Company")


