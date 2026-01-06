# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2026-01-05 20:30:38
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2026-01-06 05:57:29
"""
Test Models
"""
from datetime import datetime, timezone

from django.test import TestCase

from restaurant.models import Dish, Reservation


class TestDishModel(TestCase):
    """
    TestDishModel class
    """

    def test_string_representation_includes_name(self):
        """
        Verifies that the string representation includes the dish name
        """
        dish = Dish(name="Pizza", price=12.5)
        self.assertIn(dish.name, str(dish))

    def test_string_representation_includes_price(self):
        """
        Verifies that the string representation includes the dish price
        """
        dish = Dish(name="Pizza", price=12.5)
        self.assertIn(str(dish.price), str(dish))


class TestReservationModel(TestCase):
    """
    TestReservationModel class
    """

    def setUp(self):
        """
        Setups attributes for ReservationModel tests
        """
        reserved_at = datetime(2025, 1, 1, tzinfo=timezone.utc)

        self.formatted_reserved_at = reserved_at.strftime("%H:%M %d-%m-%Y")
        self.reseveration = Reservation(
            first_name="John",
            last_name="Doe",
            no_guests=2,
            reserved_at=reserved_at,
            comment="",
        )

    def test_string_representation_includes_first_name(self):
        """
        Verifies that the string representation includes first name
        """
        self.assertIn(self.reseveration.first_name, str(self.reseveration))

    def test_string_representation_includes_last_name_uppercase(self):
        """
        Verifies that the string representation includes last name in uppercase
        """
        # pylint: disable=no-member
        self.assertIn(self.reseveration.last_name.upper(), str(self.reseveration))

    def test_string_representation_includes_no_guests(self):
        """
        Verifies that the string representation includes number of guests
        """
        self.assertIn(str(self.reseveration.no_guests), str(self.reseveration))

    def test_string_representation_includes_formatted_reserved_at(self):
        """
        Verifies that the string representation includes reserved at in %H:%M %d-%m-%Y format
        """
        self.assertIn(self.formatted_reserved_at, str(self.reseveration))
