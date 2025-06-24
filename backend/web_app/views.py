import pandas as pd
import plotly.express as px
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from web_app.forms import DateForm
from web_app.models import House_Prices

from .forms import RegistrationForm


@login_required(login_url="/login")
def charts(request):
    """View to display charts on the charts page"""
    start = request.GET.get("start")
    end = request.GET.get("end")

    qs = House_Prices.objects.all()
    if start:
        qs = qs.filter(date__gte=start)
    if end:
        qs = qs.filter(date__lte=end)

    df = pd.DataFrame.from_records(
        qs.values("date", "detached_average_price", "region_name")
    )

    if df.empty:
        print("no data")
    else:
        fig = px.line(
            df,
            x="date",
            y="detached_average_price",
            color="region_name",
            title="Detached House Prices Over Time",
            labels={"x": "Date", "y": "Average Price in £"},
        )

    fig.update_layout(title={"font_size": 24, "xanchor": "center", "x": 0.5})

    chart = fig.to_html()
    context = {"chart": chart, "form": DateForm()}
    return render(request, "main/charts.html", context)


def home(request):
    return render(request, "main/home.html")


def sign_up(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/home")
    else:
        form = RegistrationForm()

    return render(request, "registration/sign_up.html", {"form": form})
