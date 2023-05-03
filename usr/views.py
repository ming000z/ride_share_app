from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import (
  CreateView,
  DetailView,
  ListView,
  UpdateView,
)

from .forms import UsrUpdateForm, UsrDeleteOrderForm
from main.models import (Profile, Order, User)
# Create your views here.


def usr_order_detail_view(request,id):

  try:
    orders = Order.objects.get(id=id)
  except Profile.DoesNotExist:
    orders = None

  try:
    driver = User.objects.get(id=orders.driver_id)
    profile = Profile.objects.get(user=driver)

  except User.DoesNotExist:
    driver = None
    profile = None

  context = {
    'profile': profile,
    'orders' : orders,
    'driver': driver,


  }
  return render(request, 'usr/usr_order_detail.html', context)

class UsrProfileView(DetailView):
  template_name = 'usr/usr_profile.html'
  
  def get_object(self):
    id_ = self.kwargs.get("id")
    return get_object_or_404(Profile, id=id_) 
  

class UsrUpdateView(UpdateView):
  template_name = 'usr/usr_order_update.html'
  form_class = UsrUpdateForm
  model = Order
  
  def get_object(self):
    id_ = self.kwargs.get("id")
    return get_object_or_404(Order, id=id_)
  
  def form_valid(self, form):
    return super().form_valid(form)
  
  def get_success_url(self):
    return reverse('main:main-home')
  
class UsrDeleteView(UpdateView):
  template_name = 'usr/usr_order_delete.html'
  form_class = UsrDeleteOrderForm
  model = Order
  
  def get_object(self):
    id_ = self.kwargs.get("id")
    return get_object_or_404(Order, id=id_)
  
  def get_success_url(self):
    return reverse('main:main-home')
  
  def form_valid(self, form):
    form.instance.trip_status = 5
    return super().form_valid(form)
  
