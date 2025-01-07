from rest_framework import viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Company
from core.serializers import CompanySerializer, RegisterSerializer, LoginSerializer

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


class LoginAPIView(APIView):
    def post(self, request):
        data = request.data
        serializer = LoginSerializer(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=serializer.data['username'], password=serializer.data['password'])
        token = Token.objects.get_or_create(user=user)

        return Response({'token': str(token)})


class RegistrationAPIView(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def list(self, request, **kwargs):
        search = self.request.query_params.get('search', None)
        queryset = self.queryset.filter(name__startswith=search)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
