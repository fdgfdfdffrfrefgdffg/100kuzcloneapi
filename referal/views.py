from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Referal
from .serializers import ReferalSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class UserReferalsView(APIView):
    def get(self, request, user_id):
        referals = Referal.objects.filter(user=user_id)
        serializer = ReferalSerializer(referals, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ProductReferalsView(APIView):
    def get(self, request, product):
        referals = Referal.objects.filter(product=product)
        serializer = ReferalSerializer(referals, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ReferalListCreateView(ListCreateAPIView):
    queryset = Referal.objects.all()
    serializer_class = ReferalSerializer

class ReferalRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Referal.objects.all()
    serializer_class = ReferalSerializer
