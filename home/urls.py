from django.urls import path,include
from .views import *

urlpatterns = [
    path('car_list/', CarViewSet.as_view(), name='car_list'),
    

]