from django import forms
from apps.mascota.models import Mascota
import time
class MascotaForm(forms.ModelForm):
    class Meta:
        CHOICES = (('Male','Male'),('Female','Female'))
        model=Mascota

        fields = [
            'nombre',
            'sexo',
            'edad_aproximada',
            'fecha_rescate',
            'persona',
            'vacuna',
        ]

        labels = {
            'nombre': 'Nombre',
            'sexo': 'Sexo',
            'edad_aproximada': 'Edad Aproximada',
            'fecha_rescate': 'Fecha de Rescate',
            'persona': 'Adoptante',
            'vacuna': 'Vacunas',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'sexo': forms.Select(choices=CHOICES, attrs={'class':'form-control'}),
            'edad_aproximada': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_rescate': forms.SelectDateWidget(years=range(1,int(time.strftime("%Y"))+1), attrs={'class': 'form-control'}),
            'persona': forms.Select(attrs={'class':'form-control'}),
            'vacuna': forms.CheckboxSelectMultiple(),
        }