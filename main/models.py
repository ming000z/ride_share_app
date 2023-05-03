from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.urls import reverse


# Create your models here.
class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  is_driver = models.BooleanField(default=False)
  
  class CARTYPE(models.TextChoices):
    NA = '1', 'N/A'
    SEDAN = '2', 'SEDAN'
    COUPE = '3', 'COUPE'
    SUV  = '4', 'SUV'
    MPV = '5', 'MPV'
    


  type = models.CharField(max_length=10, choices=CARTYPE.choices, default=CARTYPE.NA) 
  plante_num = models.CharField(max_length=10, blank=True, null=True, default=None)
  max_passenger = models.IntegerField(default=0)
  available_status = models.BooleanField(default=True)#ongoing
  special_info = models.TextField(blank=True, null=True, default=None)
  
  def get_profile_url(self):
    return reverse('driver:driver-profile', kwargs={'id': self.id})
  
  def get_update_url(self):
    return reverse('driver:driver-update', kwargs={'id': self.id})

  def get_absolute_url(self):
    return reverse('driver:driver-main', kwargs={'id': self.id})

class Order(models.Model):
  #id = request_id
  destination = models.CharField(max_length=500)
  arrival_time = models.DateTimeField()
  total_passenger = models.IntegerField()
  can_share = models.BooleanField(default=False)
  
  class Trip_State(models.IntegerChoices):
    COMPLETE = 4
    IN_TRIP = 3
    CONFIRMED = 2
    OPEN = 1
    CANEL = 5
  
  rider_id = models.IntegerField(default=0)
  driver_id = models.IntegerField(default=None, null=True)
  trip_status = models.IntegerField(choices=Trip_State.choices, default=Trip_State.OPEN)
  # share_id is share name
  share_ids = ArrayField(models.CharField(max_length=200), blank=True, default=list)
  
class Share(models.Model):
  rider_id = models.IntegerField(default=0)
  # share_id is share name
  share_id = models.CharField(max_length=50)
  share_passsenger = models.IntegerField(default=0)
  order_id = models.IntegerField(default=0)
