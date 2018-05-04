from django.forms import ModelForm
from maintainer.models import titanic

class titanic_form(ModelForm):
    class Meta:
        model = titanic
        fields = '__all__'
