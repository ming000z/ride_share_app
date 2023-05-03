from django import forms

from main.models import Share, Order


    
class ShareJoinOrderForm(forms.ModelForm):
  pass_num = forms.IntegerField(help_text="How many people to join?")
  class Meta:
    model = Order
    fields = ['destination', 'arrival_time', 'total_passenger']
    
  def __init__(self, *args, **kwargs):
    self.user = kwargs.pop('user')
    super().__init__(*args, **kwargs)
    self.fields['destination'].disabled = True
    self.fields['arrival_time'].disabled = True
    self.fields['total_passenger'].disabled = True
    
  
  def save(self, commit: bool = True):
    instance = super().save(commit=False)
    instance.total_passenger += int(self.data.get('pass_num'))
    instance.share_ids.append(self.user)
    Share.objects.create(rider_id=instance.rider_id, share_id=self.user, order_id=instance.pk,share_passsenger=int(self.data.get('pass_num')))
    if commit:
        instance.save()
    return instance
  
  
class ShareCancelForm(forms.ModelForm):
  
  class Meta:
    model = Order
    fields = ['destination', 'arrival_time']
    
  def __init__(self, *args, **kwargs):
    self.user = kwargs.pop('user')
    super().__init__(*args, **kwargs)
    self.fields['destination'].disabled = True
    self.fields['arrival_time'].disabled = True
    
    
  
  def save(self, commit: bool = True):
    instance = super().save(commit=False)
    share_pass = Share.objects.get(order_id=instance.id).share_passsenger
    instance.total_passenger -= int(share_pass)
    user_name = str(self.user)
    instance.share_ids.remove(user_name)
    if commit:
        instance.save()
    return instance