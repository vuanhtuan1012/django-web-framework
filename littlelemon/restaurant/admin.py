# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2026-01-03 19:57:40
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2026-01-04 12:35:42
"""
Admin module
"""
from django.contrib import admin

from .models import Dish, Reservation


class DishAdmin(admin.ModelAdmin):
    """
    ReservationAdmin class
    """

    list_display = ("name", "price")


class ReservationAdmin(admin.ModelAdmin):
    """
    ReservationAdmin class
    """

    list_display = (
        "first_name",
        "last_name",
        "guests_display",
        "reserved_at",
        "created_at",
    )

    def guests_display(self, obj):
        """
        Returns number of guests
        """
        return obj.no_guests

    guests_display.short_description = "Number of Guests"


admin.site.register(Dish, DishAdmin)
admin.site.register(Reservation, ReservationAdmin)
