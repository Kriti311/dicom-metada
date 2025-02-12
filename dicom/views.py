from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import os
from dicom.forms import DicomUploadForm
from dicom.models import DicomImage
from dicom.services.dicom import extract_dicom_metadata
from django.db.models import Q
from django.core.paginator import Paginator


@login_required
def upload_dicom(request):
    if request.method == "POST":
        form = DicomUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Read the file from memory (without saving)
            dicom_file = request.FILES["file"]

            # Extract metadata directly from the uploaded file
            metadata = extract_dicom_metadata(dicom_file)
            if metadata:
                # Create a DICOM instance without storing the file
                dicom_instance = form.save(commit=False)  # Don't save yet
                dicom_instance.user = request.user

                # Store metadata in the model fields
                for key, value in metadata.items():
                    setattr(dicom_instance, key, value)

                dicom_instance.file = None  # ✅ Prevent file from saving
                dicom_instance.save()  # Save only metadata (not the file)

                messages.success(
                    request, "DICOM metadata extracted and saved successfully!"
                )
                return redirect("dicom:list")
            else:
                messages.error(
                    request, "Invalid DICOM file or metadata extraction failed"
                )

    else:
        form = DicomUploadForm()

    return render(request, "dicom/upload.html", {"form": form})


@login_required
def dicom_list(request):
    query = request.GET.get("q")
    dicom_files = DicomImage.objects.filter(user=request.user).order_by("-upload_date")

    if query:
        dicom_files = dicom_files.filter(
            Q(patient_id__icontains=query)
            | Q(patient_name__icontains=query)
            | Q(modality__icontains=query)
        )

    # Pagination (8 results per page)
    paginator = Paginator(dicom_files, 8)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "dicom/list.html", {"dicom_files": page_obj, "query": query})


@login_required
def dicom_detail(request, pk):
    dicom_file = DicomImage.objects.get(pk=pk, user=request.user)
    return render(request, "dicom/detail.html", {"dicom": dicom_file})


@login_required
def delete_dicom(request, pk):
    dicom_file = get_object_or_404(DicomImage, pk=pk, user=request.user)

    if request.method == "POST":
        dicom_file.delete()
        messages.success(request, "DICOM file deleted successfully.")
        return redirect("dicom:list")

    return render(request, "dicom/delete_confirm.html", {"dicom_file": dicom_file})
