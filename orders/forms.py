from django import forms
from .models import OrderInfoForm


class OrdersForm(forms.ModelForm):
    delivery_date = forms.DateField(
        label="Дата доставки",
        required=True,
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    class Meta:
        model = OrderInfoForm
        fields = ['user', 'instagram', 'phone', 'add_info', 'delivery_date']
