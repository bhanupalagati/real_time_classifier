from django.forms import ModelForm
from gre.models import gre

class gre_form(ModelForm):
    class Meta:
        model = gre
        fields = '__all__'
