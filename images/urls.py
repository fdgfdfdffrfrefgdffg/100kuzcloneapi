from django.urls import path
from .views import ImageListCreateView, ImageRetrieveUpdateDestroyView

urlpatterns = [
    path('', ImageListCreateView.as_view(), name='image-list-create'),
    path('<int:pk>/', ImageRetrieveUpdateDestroyView.as_view(), name='image-detail'),
]
