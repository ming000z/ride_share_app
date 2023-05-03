from django.urls import path
from .views import (UsrProfileView, 
                    usr_order_detail_view, 
                    UsrUpdateView,
                    UsrDeleteView)

app_name = 'usr'

urlpatterns = [
  path('<int:id>/profile', UsrProfileView.as_view() , name='usr-profile'),
  path('order-update/<int:id>', UsrUpdateView.as_view(), name='usr-order-update'),
  path('order-detail/<int:id>', usr_order_detail_view, name='usr-order-detail'),
  path('order-delete/<int:id>', UsrDeleteView.as_view(), name='usr-order-delete'),
]