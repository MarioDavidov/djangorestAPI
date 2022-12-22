from django.urls import path

from companies_api.views import CompanyListApiView, CompanyDetailsApiView, EmployeeListApiView, EmployeeDetailsApiView

urlpatterns = [
    path('companies/', CompanyListApiView.as_view(), name='company list api'),
    path('companies/<int:pk>/', CompanyDetailsApiView.as_view(), name='company details api'),
    path('employee/', EmployeeListApiView.as_view(), name='employee list api'),
    path('employee/<int:pk>/', EmployeeDetailsApiView.as_view(), name='employee details api'),

]
