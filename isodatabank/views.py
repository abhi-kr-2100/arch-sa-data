from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from .forms import DataForm


class HomePageView(TemplateView):
    template_name = "isodatabank/home.html"


class UploadDataView(FormView):
    template_name = "isodatabank/upload_data.html"
    form_class = DataForm
    success_url = '/'

    def form_valid(self, form):
        return super().form_valid(form)
