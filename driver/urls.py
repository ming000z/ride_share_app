from django.urls import path

from .views import (DriverUpdateView, 
                    DriverProfileView, 
                    DriverHomeView, 
                    DriverSearchView,
                    DriverAcceptOrderView,
                    DriverCompleteOrder,
                    DriverBeginOrder,
                    driver_send_email,
                    driver_inactive)

app_name = 'driver'
urlpatterns = [
  path('<int:pk>', DriverHomeView.as_view(), name='driver-main'),
  path('<int:pk>/profile', DriverProfileView.as_view(), name='driver-profile'),
  path('<int:id>/signup', DriverUpdateView.as_view(), name='driver-update'),
  path('<int:id>/inactive',driver_inactive, name='driver-inactive'),

  path('find-order', DriverSearchView.as_view(), name='driver-find'),
  path('accept-order/<int:id>', DriverAcceptOrderView.as_view(), name="driver-accpet-order"),
  path('complete-order/<int:id>', DriverCompleteOrder.as_view(), name="driver-complete-order"),
  path('begin-order/<int:id>', DriverBeginOrder.as_view(), name="driver-begin-order"),
  path('send-email/<int:id>', driver_send_email, name="driver-send-email"),
]