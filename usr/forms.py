from django import forms

from main.models import Profile, Order

class UsrUpdateForm(forms.ModelForm):
  class Meta:
    model = Order
    fields = ['destination', 'arrival_time', 'total_passenger', 'can_share']
    
    
class UsrDeleteOrderForm(forms.ModelForm):
  class Meta:
    model = Order
    fields = ['destination', 'arrival_time', 'total_passenger']
    
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['destination'].disabled = True
    self.fields['arrival_time'].disabled = True
    self.fields['total_passenger'].disabled = True