from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.Employee_view, name='all_employees'),
    path('create_employee/', views.create_view),
    path('employees/<int:id>/', views.detail_view, name='detail_view'),
    path('employees/<int:id>/delete/', views.delete_view, name='delete_view'),
    path('employees/<int:id>/update/', views.update_view, name='update_view'),

]