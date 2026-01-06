# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2026-01-05 21:04:34
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2026-01-06 05:40:32
"""
Test Forms
"""
from datetime import datetime, timedelta, timezone
from unittest.mock import patch

from django.test import TestCase

from restaurant.forms import ReservationForm


class TestReservationForm(TestCase):
    """
    ReservationFormTest class
    """

    def setUp(self) -> None:
        """
        Setups attributes for ReservationForm tests
        """
        self.fake_now = datetime(2025, 1, 1, tzinfo=timezone.utc)
        self.yesterday = self.fake_now - timedelta(days=1)
        self.reserved_at = self.fake_now + timedelta(days=1)

    def test_form_is_valid_with_correct_data(self):
        """
        Verifies that the form validates successfully with correct input data
        """
        with patch("restaurant.forms.timezone.now", return_value=self.fake_now):
            form = ReservationForm(
                data={
                    "first_name": "John",
                    "last_name": "Doe",
                    "no_guests": 2,
                    "reserved_at": self.reserved_at,
                    "comment": "",
                }
            )
            self.assertEqual(form.is_valid(), True)

    def test_form_is_invalid_with_incorrect_first_name(self):
        """
        Verifies that the form fails validation when the first name is incorrect
        """
        with patch("restaurant.forms.timezone.now", return_value=self.fake_now):
            form = ReservationForm(
                data={
                    "first_name": "  ",
                    "last_name": "Doe",
                    "no_guests": 2,
                    "reserved_at": self.reserved_at,
                    "comment": "",
                }
            )
            self.assertEqual(form.is_valid(), False)

    def test_form_is_invalid_with_incorrect_last_name(self):
        """
        Verifies that the form fails validation when the last name is incorrect
        """
        with patch("restaurant.forms.timezone.now", return_value=self.fake_now):
            form = ReservationForm(
                data={
                    "first_name": "John",
                    "last_name": "",
                    "no_guests": 2,
                    "reserved_at": self.reserved_at,
                    "comment": "",
                }
            )
            self.assertEqual(form.is_valid(), False)

    def test_form_is_invalid_with_incorrect_no_guests(self):
        """
        Verifies that the form fails validation when the number of guests is incorrect
        """
        with patch("restaurant.forms.timezone.now", return_value=self.fake_now):
            form = ReservationForm(
                data={
                    "first_name": "John",
                    "last_name": "Doe",
                    "no_guests": -2,
                    "reserved_at": self.reserved_at,
                    "comment": "",
                }
            )
            self.assertEqual(form.is_valid(), False)

    def test_form_is_invalid_with_incorrect_reserved_at(self):
        """
        Verifies that the form fails validation when the reserved at is incorrect
        """
        with patch("restaurant.forms.timezone.now", return_value=self.fake_now):
            form = ReservationForm(
                data={
                    "first_name": "John",
                    "last_name": "Doe",
                    "no_guests": 2,
                    "reserved_at": self.yesterday,
                    "comment": "",
                }
            )
            self.assertEqual(form.is_valid(), False)

    def test_text_inputs_are_trimmed_in_cleaned_data(self):
        """
        Verifies that text inputs are trimmed of leading and trailing whitespace
        in the cleaned data
        """
        with patch("restaurant.forms.timezone.now", return_value=self.fake_now):
            form = ReservationForm(
                data={
                    "first_name": " John     ",
                    "last_name": "     Doe   ",
                    "no_guests": 2,
                    "reserved_at": self.reserved_at,
                    "comment": "   window-side, indoor table ",
                }
            )
            self.assertEqual(form.is_valid(), True)
            self.assertEqual(form.cleaned_data["first_name"], "John")
            self.assertEqual(form.cleaned_data["last_name"], "Doe")
            self.assertEqual(form.cleaned_data["no_guests"], 2)
            self.assertEqual(form.cleaned_data["reserved_at"], self.reserved_at)
            self.assertEqual(form.cleaned_data["comment"], "window-side, indoor table")
