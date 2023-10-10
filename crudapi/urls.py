
from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('create/', views.add_customer_with_details, name='add-customer'),
    path('all/',views.view_the_customers_list, name='view-customer'),
    path('all/<int:pk>/',views.view_the_customers_list, name='view-customer'),
    path('update/<int:pk>/', views.update_customer_details, name='update-customer'),
    path('customer/<int:pk>/delete/', views.delete_customer_details, name='delete-customer'),
]