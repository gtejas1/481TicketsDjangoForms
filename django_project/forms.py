from django import forms
from .models import Region

class HistoryFilterForm(forms.Form):
    region = forms.ModelChoiceField(queryset=Region.objects.all())
    day = forms.ChoiceField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')])
