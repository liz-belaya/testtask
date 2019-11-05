from django import forms

from .models import Qr

class QrForm(forms.ModelForm):

    class Meta:
        model = Qr
        fields = ('name','city','campaign','sourse','product','image')
