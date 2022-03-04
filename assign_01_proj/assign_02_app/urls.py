from django.urls import path
from . import views

app_name = "assign_02_app"
urlpatterns = [
   # Assign 1 - Excercise 1 - Create 2 view
   # Generic View
   path('ex1/', views.IndexView.as_view(), name='index'),
   path('ex1/<int:pk>/', views.DetailView.as_view(), name='detail'),

   # Assign 2 - Excercise 2 - Create 2 template
   path('ex2/', views.index, name='index'),
   path('ex2/<int:person_id>/', views.detail, name='detail'),

   # Assign 3 - Form input
   path('', views.formInput, name='formInput')
]
