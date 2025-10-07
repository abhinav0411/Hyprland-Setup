from django import forms

from .models import Reservations

class ReservationClass(forms.ModelForm)
    class Meta:
        model = Reservations
        fields = '__all__'