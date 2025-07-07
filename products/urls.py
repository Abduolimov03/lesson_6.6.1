from django.urls import path
from .views import *

urlpatterns = [
    path('car/', CarList.as_view(), name='car'),
    path('car<int:pk>/', CarDetail.as_view(), name='car-detail'),
    path('camera/create/', CarCreate.as_view(), name='create-car'),
    path('car/update/<int:pk>/', CarUpdate.as_view(), name='update-car'),
    path('car/delete/<int:pk>/', CarDelete.as_view(), name='delete-car'),
]

