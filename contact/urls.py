from django.urls import path
from.views import *


urlpatterns = [
    path('', ContactListCreateAPIView.as_view(), name='contact-list-create'),
]