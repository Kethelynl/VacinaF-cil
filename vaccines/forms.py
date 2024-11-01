from django import forms
from .models import Vaccines, MarcVaccine

class VaccineForm(forms.ModelForm):
    class Meta:
        model = Vaccines
        fields = ['name_vacinne', 'description', 'age_group', 'doses']
        
class MarcVaccineForm(forms.ModelForm):
    class Meta:
        model = MarcVaccine
        fields = ['vaccines', 'last_date', 'next_dose']