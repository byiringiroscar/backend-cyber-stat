from .serializers import ContactSerializer
from rest_framework.generics import ListCreateAPIView

# Create your views here.


class ContactListCreateAPIView(ListCreateAPIView):
    serializer_class = ContactSerializer
    queryset = ContactSerializer.Meta.model.objects.all()