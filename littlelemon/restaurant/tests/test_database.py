# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2026-01-05 22:01:55
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2026-01-05 22:07:29
"""
Test Database
"""
from datetime import datetime, timezone
from django.test import TestCase

from restaurant.models import Dish, Reservation


class DishTest(TestCase):
    """
    DishTest
    """

    def test_dish_create(self):
        """
        Tests dish create
        """
        # pylint: disable=no-member
        Dish.objects.create(name="Pizza", price=10.5)
        self.assertEqual(Dish.objects.count(), 1)

class ReservationTest(TestCase):
    """
    ReservationTest
    """

    def test_reservation_create(self):
        """
        Tests reservation create
        """
        # pylint: disable=no-member
        Reservation.objects.create(
            first_name="John",
            last_name="Doe",
            no_guests=2,
            reserved_at=datetime(2025, 1, 1, tzinfo=timezone.utc),
            comment="",
        )
        self.assertEqual(Reservation.objects.count(), 1)
