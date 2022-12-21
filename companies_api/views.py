from django.shortcuts import render
from rest_framework import views as rest_views, status
from rest_framework.response import Response
from companies_api.models import Companies
from companies_api.serialize import CompanySerializer


class CompanyApiView(rest_views.APIView):
    def get(self, request):
        company = Companies.objects.all()
        serializer = CompanySerializer(company, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CompanySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class CompanyDetailsApiView(rest_views.APIView):
    def get(self, request, pk):
        company = Companies.objects.get(pk=pk)
        serializer = CompanySerializer(company, many=False)
        return Response(serializer.data)

    def post(self, request, pk):
        company = Companies.objects.get(pk=pk)
        serializer = CompanySerializer(company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        company = Companies.objects.get(pk=pk)
        company.delete()
        return Response(status=status.HTTP_200_OK)
