from django.urls import path

from .views import HomePageView, UploadDataView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('upload/', UploadDataView.as_view(), name='upload'),
]
