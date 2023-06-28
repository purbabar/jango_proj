from django.urls import path
from . import views

urlpatterns = [
    path('uptime', views.print_linux_uptime, name='uptime')
]


