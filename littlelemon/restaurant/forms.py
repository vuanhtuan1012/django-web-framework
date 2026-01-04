# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2026-01-04 01:21:24
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2026-01-04 17:42:58
"""
Forms module
"""
from typing import Any

from django import forms
from django.utils import timezone

from .models import Reservation


class ReservationForm(forms.ModelForm):
    """
    ReservationForm class
    """
    class Meta:  # pylint: disable=R0903, C0115
        model = Reservation
        fields = ("first_name", "last_name", "no_guests", "reserved_at", "comment")

    def is_valid(self) -> bool:
        if not super().is_valid():
            return False

        # handles a past datetime
        reserved_at = self.cleaned_data.get("reserved_at")
        if reserved_at and reserved_at < timezone.now():
            self.add_error(
                None, "Sorry, you cannot make a reservation for a past date and time."
            )
            return False

        return True

    def clean(self) -> dict[str, Any]:
        """
        Removes leading and trailing whitespace from the input
        of CharField and TextField fields.
        """
        cleaned_data = super().clean()
        for field_name, value in cleaned_data.items():
            field = self.fields.get(field_name)
            if isinstance(field, forms.CharField) and isinstance(value, str):
                cleaned_data[field_name] = value.strip()
        return cleaned_data
