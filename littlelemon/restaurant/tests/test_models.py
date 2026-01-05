# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2026-01-05 20:30:38
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2026-01-05 22:11:18
"""
Test Models
"""
from datetime import datetime, timezone

from django.db import IntegrityError, transaction
from django.test import TestCase

from restaurant.models import Dish, Reservation


class DishModelTest(TestCase):
    """
    DishModelTest
    """

    def test_string_representation(self):
        """
        Tests string representation
        """
        instance = Dish(name="Pizza", price=12.5)
        self.assertEqual(str(instance), "Pizza, 12.5€")

    def test_name_unique(self):
        """
        Tests name unique
        """
        # pylint: disable=no-member
        Dish.objects.create(name="Pizza", description="Tasty", price=10.5)
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                Dish.objects.create(name="Pizza", description="Duplicate", price=12.5)


class ReservationModelTest(TestCase):
    """
    ReservationModelTest
    """

    def test_string_representation(self):
        """
        Tests string representation
        """
        reserved_at = datetime(2025, 1, 1, tzinfo=timezone.utc)
        str_reserved_at = reserved_at.strftime("%H:%M %d-%m-%Y")
        instance = Reservation(
            first_name="John",
            last_name="Doe",
            no_guests=2,
            reserved_at=reserved_at,
            comment="",
        )
        self.assertEqual(
            str(instance),
            f"John DOE, 2 guests, reserved at {str_reserved_at}",
        )
