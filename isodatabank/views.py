from typing import List
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.views.generic.list import ListView

from .forms import DataForm
from .models import Data


class HomePageView(TemplateView):
    template_name = "isodatabank/home.html"


class UploadDataView(FormView):
    template_name = "isodatabank/upload_data.html"
    form_class = DataForm
    success_url = '/'

    def add_to_db(self, file):
        pass

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        file = request.FILES['tilia_template_file']
        if form.is_valid():
            try:
                self.add_to_db(file)
            except Exception:
                return self.form_invalid(form)
                
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

class DataListView(ListView):
    model = Data
    paginate_by = 100

    def get_context_data(self, **kwargs):
        return {}
