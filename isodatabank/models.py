from typing import SupportsRound
from django.db import models


class Data(models.Model):
    site_name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.FloatField()


class BackgroundInfo(models.Model):
    site_name = models.CharField(
        verbose_name="Site Name [Archaeological ID]",
        max_length=100)
    latitude = models.FloatField(verbose_name="Latitude (in degrees)")
    longitude = models.FloatField(verbose_name="Longitude (in degrees)")
    exact = models.BooleanField(verbose_name="Are these exact coordinates?")
    altitude = models.FloatField(verbose_name="Altitude (in metres)")
    site_description = models.TextField()

    # TODO: use the correct data type for the following fields
    collection_unit_type = models.CharField(max_length=100)
    collection_unit_name = models.CharField(max_length=100)
    depositional_environment = models.TextField()

    # identifies which Tilia form this model is associated with
    source_id = models.CharField(max_length=100, editable=False)


class SpecimenInfo(models.Model):
    specimen_id = models.CharField(max_length=100)
    genus_and_species = models.CharField(max_length=200)
    broad_group = models.CharField(max_length=100)
    element = models.CharField(max_length=100)
    symmetry = models.CharField(max_length=100)
    portion = models.CharField(max_length=100)
    maturity = models.CharField(max_length=100)
    sex = models.CharField(max_length=100)
    associated_collection_unit = models.CharField(max_length=100)
    direct_c14_date = models.CharField(max_length=100)

    # identifies which Tilia form this model is associated with
    source_id = models.CharField(max_length=100, editable=False)


class ChronologiesInfo(models.Model):
    collection_unit = models.CharField(max_length=100)
    age_unit = models.CharField(max_length=100)
    older_bound = models.CharField(max_length=100)
    younger_bound = models.CharField(max_length=100)
    age_basis = models.CharField(max_length=100)
    age_basis_range = models.CharField(max_length=100)

    # identifies which Tilia form this model is associated with
    source_id = models.CharField(max_length=100, editable=False)


class IsotopeInfo(models.Model):
    specimen_id = models.CharField(max_length=100)
    sample_type = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    substrate = models.CharField(max_length=100)
    isotope = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    sd = models.CharField(max_length=100, verbose_name="SD")
    c_n_ratio = models.CharField(max_length=100, verbose_name="C:N ratio")
    instrument = models.CharField(max_length=100, verbose_name="Instrument and sample induction system")
    scale = models.CharField(max_length=100)
    pre_treatment_methods = models.CharField(max_length=100, verbose_name="Pre-treatment methods")

    # identifies which Tilia form this model is associated with
    source_id = models.CharField(max_length=100, editable=False)


class PublicationInfo(models.Model):
    author = models.CharField(max_length=100)
    year = models.IntegerField()
    article_title = models.CharField(max_length=500)
    journal = models.CharField(max_length=100)
    volume = models.CharField(max_length=100)
    issue = models.CharField(max_length=100)
    pages = models.CharField(max_length=100)
    citation = models.CharField(max_length=100)
    url = models.URLField()
    doi = models.CharField(max_length=200, verbose_name="DOI")
    associated_dataset = models.CharField(max_length=200)

    # identifies which Tilia form this model is associated with
    source_id = models.CharField(max_length=100, editable=False)


class ContactInfo(models.Model):
    family_name = models.CharField(max_length=100)
    given_name = models.CharField(max_length=100)
    leading_initials = models.CharField(max_length=100)
    suffix = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)
    email = models.EmailField()
    url = models.URLField()
    address = models.TextField()
    notes = models.TextField()

class ValidationInfo(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    validated = models.BooleanField(default=False)

    # identifies which Tilia form this model is associated with
    source_id = models.CharField(max_length=100, editable=False)
