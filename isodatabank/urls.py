from django.urls import path

from .views import HomePageView, UploadDataView, DataListView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('upload/', UploadDataView.as_view(), name='upload'),
    path('browse/', DataListView.as_view(), name='browse')
]
