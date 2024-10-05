from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Accesses
from .serializers import AccessesSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class UserReferalsView(APIView):
    def get(self, request, user_id):
        referals = Accesses.objects.filter(user_id=user_id)
        serializer = AccessesSerializer(referals, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ReferalsIdView(APIView):
    def get(self, request, ref_id):
        referals = Accesses.objects.filter(ref_id=ref_id)
        serializer = AccessesSerializer(referals, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ReferalListCreateView(ListCreateAPIView):
    queryset = Accesses.objects.all()
    serializer_class = AccessesSerializer

class ReferalRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Accesses.objects.all()
    serializer_class = AccessesSerializer
