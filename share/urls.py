from django.urls import path
from .views import ShareSearchResultView, ShareHomeView, ShareJoinOrderView, SharCancelView

app_name = 'share'

urlpatterns = [
  path('', ShareHomeView.as_view(), name='share-home'),
  path('search', ShareSearchResultView.as_view(), name='share-search-result'),
  path('join/<int:id>', ShareJoinOrderView.as_view(), name='share-join'),
  path('cancel/<int:id>',SharCancelView.as_view(), name='share-cancel'),
  
  # path('<int:id>/profile', UsrProfileView.as_view() , name='usr-profile'),
  # path('order-update/<int:id>', UsrUpdateView.as_view(), name='usr-order-update'),
  # path('order-detail/<int:id>', usr_order_detail_view, name='usr-order-detail'),
  # path('order-delete/<int:id>', UsrDeleteView.as_view(), name='usr-order-delete'),
]