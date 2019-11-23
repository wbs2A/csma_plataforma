from django import forms
from .models import Denuncia


class DenunciaForm(forms.Form):
    user = forms.CharField()
    latitude = forms.FloatField()
    longitude = forms.FloatField()

    user.widget = forms.HiddenInput()
    latitude.widget = forms.HiddenInput()
    longitude.widget = forms.HiddenInput()
    class Meta:
        model = Denuncia
        fields = ('observacao', 'conhece_origem', 'contato')