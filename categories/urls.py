from django.urls import path
from .views import CategoriesListCreateView, CategoriesRetrieveUpdateDestroyView

urlpatterns = [
    path('', CategoriesListCreateView.as_view(), name='categories-list-create'),
    path('<int:pk>/', CategoriesRetrieveUpdateDestroyView.as_view(), name='categories-detail'),
]
