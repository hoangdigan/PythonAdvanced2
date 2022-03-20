from django.urls import path, include

urlpatterns = [
    path('api/', include('customers_info.api.urls'))
]