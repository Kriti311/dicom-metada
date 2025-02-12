# apps/dicom/models.py
from django.db import models
from django.conf import settings
from datetime import datetime

class DicomImage(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    file = models.FileField(upload_to='dicom_files/')
    upload_date = models.DateTimeField(auto_now_add=True)
    
    # DICOM metadata fields
    patient_id = models.CharField(max_length=64, blank=True)
    patient_name = models.CharField(max_length=200, blank=True)
    study_date = models.DateTimeField(null=True, blank=True)
    modality = models.CharField(max_length=10, blank=True)
    study_description = models.TextField(blank=True)
    series_description = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.patient_id} - {self.study_date}"
