from time import time
from django.db import models

from openpyxl import load_workbook

from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.views.generic.list import ListView

from .forms import TiliaTemplateUploadForm
from .models import LocationInformation, ValidationInformation


class HomePageView(TemplateView):
    template_name = "isodatabank/home.html"


class UploadDataView(FormView):
    template_name = "isodatabank/upload_data.html"
    form_class = TiliaTemplateUploadForm
    success_url = '/upload/success/'

    def add_to_db(self, name, email, file):
        """Add uploaded data to isodatabank's database."""

        dataset_id = str(time())
        bg_info = load_workbook(file).worksheets[0]

        validation_info = ValidationInformation(
            submission_by=name, email=email,
            dataset_id=dataset_id
        )

        location_name = str(bg_info.cell(1, 2).value).strip()
        description = str(bg_info.cell(6, 2).value).strip()
        latitude = float(bg_info.cell(2, 2).value)
        longitude = float(bg_info.cell(3, 2).value)

        location_info = LocationInformation(
            location_name=location_name, description=description,
            latitude=latitude, longitude=longitude,
            dataset_id=dataset_id
        )

        validation_info.save()
        location_info.save()
        

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        
        name = request.POST['name']
        email = request.POST['email']
        tilia_file = request.FILES['tilia_template_file']

        if form.is_valid():
            try:
                self.add_to_db(name, email, tilia_file)
            except Exception:
                return self.form_invalid(form)
                
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class UploadSuccessful(TemplateView):
    template_name = "isodatabank/upload_success.html"


class LocationListView(ListView):
    model = LocationInformation

    def get_template_names(self):
        return 'isodatabank/location_list.html'

    def get_context_data(self, **kwargs):
        validated = ValidationInformation.objects.filter(validated=True)
        locs = []
        for v in validated:
            locs += LocationInformation.objects.filter(dataset_id=v.dataset_id)

        return {'locs': locs}
