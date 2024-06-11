from rest_framework import generics
from app.models import Add
from app.api.serializers import AddSerializer
from rest_framework.authentication import  BasicAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

#представление для списка
class AddListView(generics.ListAPIView):
    queryset = Add.objects.all()
    serializer_class = AddSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

#представление для каждого элемента списка
class AddDetailView(generics.RetrieveAPIView):
    queryset = Add.objects.all()
    serializer_class = AddSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

