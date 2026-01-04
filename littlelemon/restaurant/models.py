# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2026-01-03 19:57:40
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2026-01-04 10:43:57
"""
Models module
"""
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Dish(models.Model):
    """
    Dish class
    """

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=500)
    price = models.DecimalField(
        max_digits=5, decimal_places=1, validators=[MinValueValidator(0.0)]
    )

    def __str__(self) -> str:
        return f"{self.name}, {self.price}€"


class Reservation(models.Model):
    """
    Reservation class
    """

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    no_guests = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(20)]
    )
    reserved_at = models.DateTimeField()
    comment = models.TextField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return (
            f"{self.first_name} {self.last_name.upper()}, {self.no_guests} "
            f"guests, reserved at {self.reserved_at.strftime('%H:%M %d-%m-%Y')}"
        )
