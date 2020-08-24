from django.db import models
from django_countries.fields import CountryField

COMPANY_SIZE = (
    ("1 - 10", "1 - 10"),
    ("11 - 50", "11 - 50"),
    ("51 - 100", "51 - 100"),
    ("101 - 500", "101 - 500"),
    ("501 - 1000", "501 - 1000"),
    ("Above 1000", "Above 1000")
)

SECTORS = (
        ("AGRICULTURE", "AGRICULTURE"),
        ("AVIATION", "AVIATION"),
        ("COMMERCIAL/RETAIL", "COMMERCIAL/RETAIL"),
        ("CONSTRUCTION", "CONSTRUCTION"),
        ("EDUCATION AND TRAINING", "EDUCATION AND TRAINING"),
        ("ENERGY AND POWER GENERATION", "ENERGY AND POWER GENERATION"),
        ("FMCG", "FMCG"),
        ("FASHION", "FASHION"),
        ("FINANCIAL SERVICES", "FINANCIAL SERVICES"),
        ("HAULAGE/LOGISTICS", "HAULAGE/LOGISTICS"),
        ("HEALTHCARE", "HEALTHCARE"),
        ("ICT", "ICT"),
        ("MANUFACTURING", "MANUFACTURING"),
        ("MEDIA & ENTERTAINMENT", "MEDIA & ENTERTAINMENT"),
        ("OIL & GAS", "OIL & GAS"),
        ("PROFESSIONAL SERVICES", "PROFESSIONAL SERVICES"),
        ("TELECOMMUNICATIONS", "TELECOMMUNICATIONS"),
        ("TRANSPORTATION", "TRANSPORTATION"),
        ("WASTE MANAGEMENT", "WASTE MANAGEMENT"),
    )


# Create your models here.
class MyModel(models.Model):
    organisation_sector = models.CharField(
        max_length=40,
        choices=SECTORS,
        default="1"
    )
    organisation_size = models.CharField(
        max_length=10,
        choices=COMPANY_SIZE,
        default="1"
    )
    country = CountryField()

    def __str__(self):
        return self.organisation_size
