from django.urls import path
from .views import SampleView

urlpatterns = [
    path('', SampleView)
]