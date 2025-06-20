from django.db import models


# Create your models here.
class House_Prices(models.Model):
    """model representing house prices in different regions."""

    date = models.DateField()
    region_name = models.CharField(max_length=100)
    detached_average_price = models.FloatField(null=True, blank=True)
    detached_index = models.FloatField(null=True, blank=True)
    detached_monthly_change = models.FloatField(null=True, blank=True)
    detached_annual_change = models.FloatField(null=True, blank=True)
    semi_detached_average_price = models.FloatField(null=True, blank=True)
    semi_detached_index = models.FloatField(null=True, blank=True)
    semi_detached_monthly_change = models.FloatField(null=True, blank=True)
    semi_detached_annual_change = models.FloatField(null=True, blank=True)
    terraced_average_price = models.FloatField(null=True, blank=True)
    terraced_index = models.FloatField(null=True, blank=True)
    terraced_monthly_change = models.FloatField(null=True, blank=True)
    terraced_annual_change = models.FloatField(null=True, blank=True)
    flat_average_price = models.FloatField(null=True, blank=True)
    flat_index = models.FloatField(null=True, blank=True)
    flat_monthly_change = models.FloatField(null=True, blank=True)
    flat_annual_change = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.region_name}"

    class meta:
        ordering = ("date",)
