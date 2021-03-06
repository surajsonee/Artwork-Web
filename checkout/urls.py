# This file requires url registration in project_main/urls.py
from django.urls import path  # Import url path
from . import views  # Import views
from .webhooks import webhook  # Import webhook function from .webhook


urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<order_number>',
            views.checkout_success, name='checkout_success'),
    path('cache_checkout_data/',
            views.cache_checkout_data, name='cache_checkout_data'),
    # Call webhook function in webhook.py
    path('wh/', webhook, name='webhook'),
]
