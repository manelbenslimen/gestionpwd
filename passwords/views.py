from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PasswordSerializer
from .models import Password
# Create your views here.
class PasswordViewSet(viewsets.ModelViewSet):
    queryset = Password.objects.all()
    serializer_class = PasswordSerializer