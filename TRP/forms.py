from django import forms
from TRP.models import Inform


class InformForm(forms.ModelForm):
    class Meta:
        model = Inform
        fields = ['start_date']
        labels = {
            'name': '이름',
            'start_date': '시작일',
        }