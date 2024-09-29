from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Categories
from .serializers import CategoriesSerializer

class CategoriesListCreateView(ListCreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer

class CategoriesRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
