# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2026-01-05 21:04:34
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2026-01-05 21:49:28
"""
Test Forms
"""
from datetime import datetime, timedelta, timezone
from unittest.mock import patch

from django.test import TestCase

from restaurant.forms import ReservationForm


class ReservationFormTest(TestCase):
    """
    ReservationFormTest
    """

    def setUp(self) -> None:
        """
        Setup
        """
        self.fake_now = datetime(2025, 1, 1, tzinfo=timezone.utc)
        self.yesterday = self.fake_now - timedelta(days=1)
        self.reserved_at = self.fake_now + timedelta(days=1)

    def test_form_valid(self):
        """
        Tests form valid
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

    def test_first_name_invalid(self):
        """
        Tests first name invalid
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

    def test_last_name_invalid(self):
        """
        Tests last name invalid
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

    def test_no_guests_invalid(self):
        """
        Tests number of guests invalid
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

    def test_reserved_at_invalid(self):
        """
        Tests reserved at invalid
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

    def test_form_clean(self):
        """
        Tests form clean
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
