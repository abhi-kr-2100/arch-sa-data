from django.urls import path

from .views import *


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('upload/', UploadDataView.as_view(), name='upload'),
    path('upload/success/', UploadSuccessful.as_view(), name='upload_success'),
    path('browse/', LocationListView.as_view(), name='browse'),
    path('download/<dataset_id>/', download_view, name='download'),
    path('know_more/', MoreAboutIsotopes.as_view(), name='know_more'),
]
