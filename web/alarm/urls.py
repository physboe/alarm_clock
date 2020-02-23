from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:alarm_id>/', views.detail, name='detail'),
    path('<int:alarm_id>/save/', views.save, name='save'),
    path('new/', views.new, name='new')
]
