from django import forms

from main.models import Order


class NewOrderForm(forms.ModelForm):
  class Meta:
    model = Order
    fields = [
      'destination',
      'arrival_time',
      'total_passenger',
      'can_share',
    ]
    
    widgets = {
      'arrival_time': forms.TextInput(attrs={'type': 'datetime-local'}),
    }