from django.urls import path
from .views import ReferalListCreateView, ReferalRetrieveUpdateDestroyView
from .views import UserReferalsView, ProductReferalsView

urlpatterns = [
    path('', ReferalListCreateView.as_view(), name='referal-list-create'),
    path('<int:pk>/', ReferalRetrieveUpdateDestroyView.as_view(), name='referal-detail'),
    path('user/<int:user_id>/referals/', UserReferalsView.as_view(), name='user-referals'),
    path('products/<int:product_id>/referals/', ProductReferalsView.as_view(), name='products-referals'),
]
