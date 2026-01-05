# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2026-01-03 19:57:40
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2026-01-05 08:01:01
"""
Admin module
"""
from django.contrib import admin

from .models import Dish, Reservation


class DishAdmin(admin.ModelAdmin):
    """
    DishAdmin class
    """

    list_display = ("name", "price")


class ReservationAdmin(admin.ModelAdmin):
    """
    ReservationAdmin class
    """

    list_display = (
        "first_name",
        "last_name",
        "guests",
        "reserved_at",
        "created_at",
    )

    def guests(self, obj: Reservation):
        """
        Returns number of guests
        """
        return obj.no_guests

    guests.short_description = "Number of Guests"


admin.site.register(Dish, DishAdmin)
admin.site.register(Reservation, ReservationAdmin)
