import pydicom
from datetime import datetime


def parse_dicom_date(date_string):
    """Parse DICOM date format to Python datetime"""
    if not date_string:
        return None
    try:
        return datetime.strptime(date_string, "%Y%m%d")
    except ValueError:
        return None


def extract_dicom_metadata(dicom_file):
    """Extract metadata from DICOM file"""
    try:
        ds = pydicom.dcmread(dicom_file)
        metadata = {
            "patient_id": getattr(ds, "PatientID", ""),
            "patient_name": str(getattr(ds, "PatientName", "")),
            "study_date": parse_dicom_date(getattr(ds, "StudyDate", "")),
            "modality": getattr(ds, "Modality", ""),
            "study_description": getattr(ds, "StudyDescription", ""),
            "series_description": getattr(ds, "SeriesDescription", ""),
        }
        return metadata
    except Exception as e:
        print(f"Error reading DICOM file: {str(e)}")
        return None
