from django.urls import path
from . import views

app_name = 'dicom'

urlpatterns = [
    path('list/', views.dicom_list, name='list'),
    path('upload/', views.upload_dicom, name='upload'),
    path('detail/<int:pk>/', views.dicom_detail, name='detail'),
    path('delete/<int:pk>/', views.delete_dicom, name='delete'),
]