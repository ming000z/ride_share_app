from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse

from django.utils import timezone
from django.core.mail import send_mail
from django.contrib.auth.models import User
from main.models import Profile, Order
from .forms import ProfileForm, DriverAcceptForm, DriverCompleteOrderForm
from django.views.generic import (
  CreateView,
  DetailView,
  ListView,
  UpdateView,
  DeleteView
)

# Create your views here.
class DriverUpdateView(UpdateView):
  template_name = 'driver/driver_update.html'
  form_class = ProfileForm
  queryset = Profile.objects.all()

  def get_success_url(self):
    return reverse('driver:driver-main', args=[self.request.user.id])
  
  def get_object(self):
    id_ = self.request.user.id
    return get_object_or_404(Profile, user_id=id_)
  
  def form_valid(self, form):
    form.instance.is_driver = True
    return super().form_valid(form)
  
  
class DriverProfileView(DetailView):
  template_name = 'driver/driver_profile.html'
  model = Profile

  def get_object(self):
    id_ = self.request.user.id
    return get_object_or_404(Profile, user_id=id_)
  
class DriverHomeView(DetailView):
  template_name = 'driver/driver_home.html'
  model = Profile
  
  def get_object(self):
    id_ = self.request.user.id
    return get_object_or_404(Profile, user_id=id_)
  
  def get_context_data(self, **kwargs) :
    orders = super().get_context_data(**kwargs)
    orders['driver_in_trip_order'] = Order.objects.filter(driver_id=self.request.user.id, trip_status=3)
    orders['driver_confirm_order'] = Order.objects.filter(driver_id=self.request.user.id, trip_status=2)
    return orders


class DriverSearchView(ListView):
  template_name = 'driver/driver_order.html'
  model = Order
  
  def get_context_data(self, **kwargs):
    orders = super().get_context_data(**kwargs)
    pass_num = Profile.objects.filter(user_id=self.request.user.id).values('max_passenger')
    orders['open_order'] = Order.objects.filter(trip_status=1, total_passenger__lte=pass_num).exclude(rider_id=self.request.user.id)
    return orders
  
class DriverAcceptOrderView(UpdateView):
  template_name = 'driver/driver_accept_order.html'
  form_class = DriverAcceptForm
  queryset = Order.objects.all()
  
  def get_object(self):
    id_ = self.kwargs.get("id")
    return get_object_or_404(Order, id=id_)
  
  def form_valid(self, form):
    form.instance.driver_id = self.request.user.id
    form.instance.trip_status = 2
    return super().form_valid(form)
  
  def get_success_url(self):
    return reverse('driver:driver-send-email', args=[self.kwargs.get("id")])
  

class DriverBeginOrder(UpdateView):
  template_name = 'driver/driver_begin_order.html'
  form_class =  DriverAcceptForm
  model = Order
  
  def get_object(self):
    id_ = self.kwargs.get("id")
    return get_object_or_404(Order, id=id_)
  
  def form_valid(self, form):
    form.instance.trip_status = 3
    return super().form_valid(form)
  
  def get_success_url(self):
    return reverse('driver:driver-main', args=[self.request.user.id])


class DriverCompleteOrder(UpdateView):
  template_name = 'driver/driver_complete_order.html'
  form_class = DriverCompleteOrderForm
  model = Order
  
  def get_object(self):
    id_ = self.kwargs.get("id")
    return get_object_or_404(Order, id=id_)
  
  def form_valid(self, form):
    form.instance.trip_status = 4
    return super().form_valid(form)
  
  def get_success_url(self):
    return reverse('driver:driver-main', args=[self.request.user.id])
  

def driver_send_email(request,id):
  #template_name = 'driver/driver_sned_email.html'
  email_list=[]
  order = Order.objects.get(id=id)
  email_list.append(User.objects.get(id=order.rider_id).email)

  for share_id in order.share_ids:
    email_list.append(User.objects.get(username=share_id).email)
  
  send_mail(
    "Oder update",
    "Hi, the driver accepted your order",
    "mingzhe.z0629@gmail.com",
    email_list,#receiver email include rider and sharer
  )
  return render(request, 'driver/driver_send_email.html', {})


def driver_inactive(request,id):
  #template_name = 'driver/driver_sned_email.html'
  orders = Order.objects.filter(driver_id=id, trip_status=2)
  for free_order in orders:
    free_order.driver_id = 0
    free_order.trip_status = 1
    free_order.save()
  driver = Profile.objects.get(user_id=id)
  #driver = Profile.objects.get(user_id)
  driver.is_driver=False
  driver.save()     
  return render(request, 'driver/driver_inactive.html', {})
