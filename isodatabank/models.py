from django.db import models
from django.db.utils import DatabaseError


class LocationInformation(models.Model):
    location_name = models.CharField(max_length=100)
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    dataset_id = models.CharField(max_length=50)

    def __str__(self):
        return self.location_name


class TiliaExcelFile(models.Model):
    data = models.BinaryField()

    dataset_id = models.CharField(max_length=50)

    def __str__(self):
        return self.dataset_id


class AuthorInformation(models.Model):
    name = models.CharField(max_length=100)
    
    dataset_id = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ValidationInformation(models.Model):
    validated = models.BooleanField(default=False)
    submission_by = models.CharField(max_length=100)
    email = models.EmailField()

    dataset_id = models.CharField(max_length=50)

    def __str__(self):
        s = 'Submitted by {} ({})'.format(self.submission_by, self.email)
        return s + ' (validated)' if self.validated else s + ' (unvalidated)'
