from django import forms
from TRP.models import Inform


class InformForm(forms.ModelForm):
    class Meta:
        model = Inform
        fields = ['start_date', 'files']
        labels = {
            'name': '이름',
            'start_date': '시작일',
        }