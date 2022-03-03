from django.urls import path
from . import views

app_name = "assign_02_app"
urlpatterns = [
   # Assign 2 - Excercise 1 - Create 2 views
   path('ex1/', views.index, name='index'),
   path('ex1/<int:person_id>/', views.detail, name='detail'),

   # Assign 2 - Excercise 2 - Create 2 view - use templates
   # Generic View
   path('ex2/', views.IndexView.as_view(), name='index'),
   path('ex2/<int:pk>/', views.DetailView.as_view(), name='detail'),

   # Assign 3 - Form input
   path('', views.formInput, name='formInput')
]