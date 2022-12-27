from django.urls import path

from companies_api.views import Home_Page, CompanyListApiView, CompanyDetailsApiView, EmployeeListApiView, EmployeeDetailsApiView

urlpatterns = [
    path('', Home_Page, name='home_page'),
    path('companies/', CompanyListApiView.as_view(), name='company list api'),
    path('companies/<int:pk>/', CompanyDetailsApiView.as_view(), name='company details api'),
    path('employee/', EmployeeListApiView.as_view(), name='employee list api'),
    path('employee/<int:pk>/', EmployeeDetailsApiView.as_view(), name='employee details api'),

]
