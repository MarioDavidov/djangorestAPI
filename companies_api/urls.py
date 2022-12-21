from django.urls import path

from companies_api.views import CompanyApiView, CompanyDetailsApiView

urlpatterns = [
    path('', CompanyApiView.as_view(), name='company list api'),
    path('<int:pk>/', CompanyDetailsApiView.as_view(), name='company details api'),

]