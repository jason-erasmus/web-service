import csv
import pathlib
from datetime import datetime
from itertools import islice

from django.conf import settings
from django.core.management.base import BaseCommand
from web_app.models import House_Prices


class Command(BaseCommand):
    help = "Load data from  file"

    def handle(self, *args, **kwargs):
        datafile = settings.BASE_DIR / "data" / "property_prices.csv"

        with open(datafile, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                dt = datetime.strptime(row["Date"], "%d/%m/%Y").date()

                House_Prices.objects.get_or_create(
                    date=dt,
                    region_name=row["Region_Name"],
                    detached_average_price=self.parse_float(
                        row["Detached_Average_Price"]
                    ),
                    detached_index=self.parse_float(row["Detached_Index"]),
                    detached_monthly_change=self.parse_float(
                        row["Detached_Monthly_Change"]
                    ),
                    detached_annual_change=self.parse_float(
                        row["Detached_Annual_Change"]
                    ),
                    semi_detached_average_price=self.parse_float(
                        row["Semi_Detached_Average_Price"]
                    ),
                    semi_detached_index=self.parse_float(row["Semi_Detached_Index"]),
                    semi_detached_monthly_change=self.parse_float(
                        row["Semi_Detached_Monthly_Change"]
                    ),
                    semi_detached_annual_change=self.parse_float(
                        row["Semi_Detached_Annual_Change"]
                    ),
                    terraced_average_price=self.parse_float(
                        row["Terraced_Average_Price"]
                    ),
                    terraced_index=self.parse_float(row["Terraced_Index"]),
                    terraced_monthly_change=self.parse_float(
                        row["Terraced_Monthly_Change"]
                    ),
                    terraced_annual_change=self.parse_float(
                        row["Terraced_Annual_Change"]
                    ),
                    flat_average_price=self.parse_float(row["Flat_Average_Price"]),
                    flat_index=self.parse_float(row["Flat_Index"]),
                    flat_monthly_change=self.parse_float(row["Flat_Monthly_Change"]),
                    flat_annual_change=self.parse_float(row["Flat_Annual_Change"]),
                )

    def parse_float(self, value):
        try:
            return float(value) if value.strip() else None
        except ValueError:
            return None
