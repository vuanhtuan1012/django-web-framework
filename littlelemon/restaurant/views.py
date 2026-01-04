# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2026-01-03 19:57:40
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2026-01-04 19:55:30
"""
Views module
"""
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView

from .forms import ReservationForm
from .models import Dish


class HomeView(TemplateView):
    """
    HomeView
    """

    template_name = "restaurant/home.html"


class AboutView(TemplateView):
    """
    AboutView
    """

    template_name = "restaurant/about.html"


class OpeningHoursView(TemplateView):
    """
    OpeningHoursView
    """

    template_name = "restaurant/opening_hours.html"


class DishListView(ListView):
    """
    DishListView
    """

    model = Dish
    template_name = "restaurant/menu.html"
    context_object_name = "dishes"


class DishDetailView(DetailView):
    """
    DishDetailView
    """

    model = Dish
    template_name = "restaurant/dish.html"
    context_object_name = "dish"


def reserve_table(request: HttpRequest) -> HttpResponse:
    """
    Handles reservation requests
    """
    form = ReservationForm()
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Your reservation is confirmed. We look forward to seeing you!"
            )
        else:
            messages.error(request, "Please correct the errors below:")
    return render(request, "restaurant/reserve_table.html", {"form": form})
