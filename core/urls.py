from django.urls import path, include
from core.views import CompanyViewSet, RegistrationAPIView, LoginAPIView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegistrationAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
]
