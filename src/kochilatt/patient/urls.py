from django.urls import path
from . import views

urlpatterns = [
    path('', views.PatientList.as_view(), name='index'),
    path('create/', views.PatientCreate.as_view(), name='create'),
    path('update/<int:pk>', views.PatientUpdate.as_view(), name='update'),
    path('delete/<int:pk>', views.PatientDelete.as_view(), name='delete'),
    path('<int:pk>/', views.PatientDetail.as_view(), name='detail'),

]