from django.urls import path

from .views import HomePageView, UploadDataView, DataListView, UploadSuccessful


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('upload/', UploadDataView.as_view(), name='upload'),
    path('upload/success/', UploadSuccessful.as_view(), name='upload_success'),
    path('browse/', DataListView.as_view(), name='browse'),
]
