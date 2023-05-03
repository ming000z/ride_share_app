from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import (
  CreateView,
  DetailView,
  ListView,
  UpdateView,
  TemplateView
)

from main.models import (Profile, Order, Share)
from .forms import ShareJoinOrderForm, ShareCancelForm


class ShareHomeView(TemplateView):
  template_name = 'share/share_home.html'

class ShareSearchResultView(ListView):
  model = Order
  template_name = 'share/share_search_result.html'
  
  def get_queryset(self): 
    des = self.request.GET.get("des")
    earliest_time = self.request.GET.get("earliest-time")
    latest_time = self.request.GET.get("latest-time")
    return Order.objects.filter(destination=des, 
                                arrival_time__range=(earliest_time, latest_time),
                                can_share=True,
                                trip_status=1
                                ).exclude(share_ids__contains=[self.request.user.username]
                                          ).exclude(rider_id=self.request.user.id)
    
  
class ShareJoinOrderView(UpdateView):
  template_name = 'share/share_join.html'
  form_class = ShareJoinOrderForm
  queryset = Order.objects.all()
  
  def get_form_kwargs(self):
        kwargs = super(ShareJoinOrderView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs
  
  def get_object(self):
    id_ = self.kwargs.get("id")
    return get_object_or_404(Order, id=id_)
  
  def form_valid(self, form):
    return super().form_valid(form)
  
  def get_success_url(self):
    return reverse('order:order-detail', args=[self.kwargs.get("id")])
  

class SharCancelView(UpdateView):
  template_name = 'share/share_cancel.html'
  form_class = ShareCancelForm
  queryset = Order.objects.all()
  
  def get_form_kwargs(self):
        kwargs = super(SharCancelView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs
  
  def get_object(self):
    id_ = self.kwargs.get("id")
    return get_object_or_404(Order, id=id_)
  
  def form_valid(self, form):
    return super().form_valid(form)
  
  def get_success_url(self):
    return reverse('main:main-home')
  
  

