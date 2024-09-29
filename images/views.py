from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Image
from .serializers import ImageSerializer

class ImageListCreateView(ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class ImageRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
