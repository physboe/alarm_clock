from django.urls import path

from . import views
from alarm_core.schedule_services import Runner
from .core_interface import CoreInterfaceImpl

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:alarm_id>/', views.detail, name='detail'),
    path('<int:alarm_id>/save/', views.save, name='save'),
    path('new/', views.new, name='new'),
    path('<int:alarm_id>/delete/', views.delete, name='delete')
]

Runner().run()
CoreInterfaceImpl.getInstance().putAll()
