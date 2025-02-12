from django import forms
from dicom.models import DicomImage


class DicomUploadForm(forms.ModelForm):
    class Meta:
        model = DicomImage
        fields = ['file']

