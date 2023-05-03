from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse

from django.utils import timezone

from main.models import Order
from .forms import NewOrderForm
from django.views.generic import (
  CreateView,
  DetailView,
  ListView,
  UpdateView,
  DeleteView
)

class OrderCreateView(CreateView):
  template_name = 'order/order_create.html'
  form_class = NewOrderForm
  queryset = Order.objects.all()
  

  def form_valid(self, form):
    form.instance.rider_id = self.request.user.pk
    return super().form_valid(form)
  
  def get_success_url(self):
    return reverse('main:main-home')
  

class OrderListView(ListView):
  template_name = 'order/order_list.html'
  
  def get_queryset(self):
    return Order.objects.filter(rider_id=self.request.user.pk)
  

class OrderDetailView(DetailView):
  template_name = 'order/order_detail.html'

  def get_object(self):
    id_ = self.kwargs.get("id")
    return get_object_or_404(Order, id=id_)