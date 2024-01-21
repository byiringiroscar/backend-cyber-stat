from django.urls import path
from .views import *

urlpatterns = [
    path('information/', InformationListCreateAPIView.as_view(), name='information-list-create'),
    path('information/<str:id>/', InformationRetrieveUpdateDeleteAPIView.as_view(), name='information-detail'),
]
