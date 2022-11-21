from django.urls import path

from app_emp_mgt import views

urlpatterns = [
    path('', views.master_employee, name='master'),
    path('create', views.create_employee, name='create'),
    path('edit/<int:pk>', views.edit_employee, name='edit'),
    path('delete/<int:pk>', views.delete_employee, name='delete'),
]
