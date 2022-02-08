from django.contrib import admin

from django.urls import reverse

from .models import ValidationInformation


class ValidationAdmin(admin.ModelAdmin):
    readonly_fields = ("submission_by", "email", "dataset_id")
    fields = ("submission_by", "email", "dataset_id", "validated")

    def view_on_site(self, obj):
        url = reverse("download", args=[obj.dataset_id])
        return url


admin.site.register(ValidationInformation, ValidationAdmin)
