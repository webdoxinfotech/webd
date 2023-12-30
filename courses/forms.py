
# import form class from django
from django import forms

# import GeeksModel from models.py
from courses.models import Certificate

# create a ModelForm
class CertificateForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Certificate
        fields = ['ref_id']

    def __init__(self, *args, **kwargs):
        super(CertificateForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control border-0 p-4'
            visible.field.widget.attrs['placeholder'] = 'Enter Certificate Ref. ID'