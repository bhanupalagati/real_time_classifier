from django.forms import ModelForm
from feedback.models import feedback

class feedback_form(ModelForm):
    class Meta:
        model = feedback
        fields = '__all__'
