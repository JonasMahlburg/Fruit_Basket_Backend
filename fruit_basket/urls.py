from django.urls import path
from .views import send_fruits

urlpatterns = [
    path('', send_fruits ),
]