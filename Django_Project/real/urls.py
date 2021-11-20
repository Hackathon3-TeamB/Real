from django.urls import path
from . import views
from .views import TWU

app_name = 'real'

urlpatterns = [
    path('', TWU.as_view(), name='index'),
]
