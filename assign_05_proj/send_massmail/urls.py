from django.urls import path
from .views import EmailAttachementView

app_name = 'send_massmail'
urlpatterns = [
    path('', EmailAttachementView.as_view(), name='sendmail')
]