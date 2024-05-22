from django.contrib import admin
from django.urls import path
from bot import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index),
    path('sms', views.on_message),
    path('sms-status', views.on_sms_status),
    # path('random-file', views.random_file),
]
