from django import forms
from players.models import Players
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit

class FormularzRodzicZaloguj(forms.ModelForm):
 
    class Meta:
        model = Players
        fields = ['nazwisko_rodzic','imie_rodzic','email_rodzic','telefon_rodzic',
                  'nazwisko', 'imie', 'miasto', 'kat_wiekowa', 'bieg']


class FormularzDziecko(forms.ModelForm):

    class Meta:
        model = Players
        fields = ['nazwisko', 'imie', 'miasto','kat_wiekowa', 'bieg']
