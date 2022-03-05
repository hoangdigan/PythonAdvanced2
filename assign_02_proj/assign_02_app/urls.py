from django.urls import path
from . import views

app_name = "assign_02_app"
urlpatterns = [
    #  Exercise 1 : use teamplate
    path('ex1/', views.IndexView.as_view(), name='index'),
    path('ex1/<int:person_id>/', views.DetailView.as_view(), name='detail'),


    #  Exercise 2 : use teamplate
    path('ex2/', views.index, name='index'),
    path('ex2/<int:person_id>/', views.detail, name='detail'),

    #  Exercise 3 : form input
    path('', views.formInput, name='formInput'),
]
