from rest_framework import generics
from app.models import Add
from app.api.serializers import AddSerializer

class AddListView(generics.ListAPIView):
    queryset = Add.objects.all()
    serializer_class = AddSerializer
class AddDetailView(generics.RetrieveAPIView):
    queryset = Add.objects.all()
    serializer_class = AddSerializer