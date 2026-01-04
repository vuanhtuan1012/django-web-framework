# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2026-01-03 21:02:37
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2026-01-04 20:38:10
"""
URL dispatcher
"""
from django.urls import path

from .views import (
    AboutView,
    DishDetailView,
    DishListView,
    HomeView,
    OpeningHoursView,
    reserve_table,
)

app_name = "restaurant"  # pylint: disable=invalid-name


urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("menu/", DishListView.as_view(), name="menu"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish_detail"),
    path("reserve-table/", reserve_table, name="reserve_table"),
    path("opening-hours/", OpeningHoursView.as_view(), name="opening_hours"),
]
