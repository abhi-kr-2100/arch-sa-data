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

    def form_valid(self, form):
        return super().form_valid(form)


class DataListView(ListView):
    model = Data
    paginate_by = 100

    def get_context_data(self, **kwargs):
        return {}
