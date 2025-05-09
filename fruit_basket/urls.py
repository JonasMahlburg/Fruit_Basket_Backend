from django.urls import path
# from .views import send_fruits
from .views import send_more_fruits
from .views import show_info

urlpatterns = [
    # path('', send_fruits ),
    path('', send_more_fruits),
    path('info/', show_info),
    path('fruits/info/', show_info, name='fruit_info'),

]