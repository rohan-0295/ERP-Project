# urls.py

from django.urls import path
from .views import employee_list

urlpatterns = [
    path('list/', employee_list, name='employee_list'),
]
