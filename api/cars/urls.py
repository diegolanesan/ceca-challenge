from django.urls import path
from .views import CarViewSet

urlpatterns = [
    path('cars/', CarViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('cars/<int:pk>/', CarViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'})),
    path('cars/<str:plate>', CarViewSet.as_view({
        'get': 'get_cars_by_plate'
    })),
]
