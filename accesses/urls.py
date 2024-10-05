from django.urls import path
from .views import ReferalListCreateView, ReferalRetrieveUpdateDestroyView
from .views import UserReferalsView, ReferalsIdView

urlpatterns = [
    path('', ReferalListCreateView.as_view(), name='referal-list-create'),
    path('<int:pk>/', ReferalRetrieveUpdateDestroyView.as_view(), name='referal-detail'),
    path('user/<int:user_id>/', UserReferalsView.as_view(), name='user-referals'),
    path('products/<int:ref_id>/', ReferalsIdView.as_view(), name='refs'),
]
