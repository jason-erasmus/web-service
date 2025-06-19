from django.db import models


# Create your models here.
class House_prices(models.Model):
    """Model representing house prices in different regions."""

    Date = models.DateField(primary_key=True)
    Region_Name = models.CharField(max_length=100)
    Area_Code = models.CharField(max_length=10)
    Detached_Average_Price = models.DecimalField(
        max_digits=10, decimal_places=10, null=True, blank=True
    )
    Detached_Index = models.DecimalField(
        max_digits=10, decimal_places=10, null=True, blank=True
    )
    Detached_Monthly_Change = models.DecimalField(
        max_digits=10, decimal_places=10, null=True, blank=True
    )
    Detached_Annual_Change = models.DecimalField(
        max_digits=10, decimal_places=10, null=True, blank=True
    )
    Semi_Detached_Average_Price = models.DecimalField(
        max_digits=10, decimal_places=10, null=True, blank=True
    )
    Semi_Detached_Index = models.DecimalField(
        max_digits=10, decimal_places=10, null=True, blank=True
    )
    Semi_Detached_Monthly_Change = models.DecimalField(
        max_digits=10, decimal_places=10, null=True, blank=True
    )
    Semi_Detached_Annual_Change = models.DecimalField(
        max_digits=10, decimal_places=10, null=True, blank=True
    )
    Terraced_Average_Price = models.DecimalField(
        max_digits=10, decimal_places=10, null=True, blank=True
    )
    Terraced_Index = models.DecimalField(
        max_digits=10, decimal_places=10, null=True, blank=True
    )
    Terraced_Monthly_Change = models.DecimalField(
        max_digits=10, decimal_places=10, null=True, blank=True
    )
    Terraced_Annual_Change = models.DecimalField(
        max_digits=10, decimal_places=10, null=True, blank=True
    )
    Flat_Average_Price = models.DecimalField(
        max_digits=10, decimal_places=10, null=True, blank=True
    )
    Flat_Index = models.DecimalField(
        max_digits=10, decimal_places=10, null=True, blank=True
    )
    Flat_Monthly_Change = models.DecimalField(
        max_digits=10, decimal_places=10, null=True, blank=True
    )
    Flat_Annual_Change = models.DecimalField(
        max_digits=10, decimal_places=10, null=True, blank=True
    )

    def __str__(self):
        return f"{self.Region_Name}"
