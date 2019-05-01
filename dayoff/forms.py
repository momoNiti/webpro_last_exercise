from django import forms
import datetime
from .models import DayOff

class RequestModelForm(forms.ModelForm):
    type = forms.ChoiceField(widget=forms.RadioSelect, choices=DayOff.TYPES)
    approve_status = forms.ChoiceField(widget=forms.HiddenInput, required=False)
    date_start = forms.DateField(initial="dd/mm/yyyy", input_formats=['%d/%m/%Y'])
    date_end = forms.DateField(initial="dd/mm/yyyy", input_formats=['%d/%m/%Y'])
    class Meta:
        model = DayOff
        exclude = ['create_by']
    def clean_date_start(self):
        data = self.cleaned_data['date_start']
        if data < datetime.date.today():
            raise forms.ValidationError("ไม-่สามารถเลือกวันในอดีตได้")
        print(data)
        return data
    def clean_date_end(self):
        data = self.cleaned_data['date_end']
        if data < datetime.date.today():
            raise forms.ValidationError("ไม่สามารถเลือกวันในอดีตได้")
        return data
    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get('date_start')
        end = cleaned_data.get('date_end')
        if str(end) < str(start):
            self.add_error('date_start', 'วันไม่ถูกต้อง')
            self.add_error('date_end', 'วันไม่ถูกต้อง')