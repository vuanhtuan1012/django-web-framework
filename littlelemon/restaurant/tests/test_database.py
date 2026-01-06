# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2026-01-05 22:01:55
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2026-01-06 05:40:04
"""
Test Database
"""
from datetime import datetime, timezone

from django.db import IntegrityError, transaction
from django.test import TestCase

from restaurant.models import Dish, Reservation


class TestDishModel(TestCase):
    """
    TestDishModel class
    """

    def test_creates_dish_when_data_is_valid(self):
        """
        Verifies that a dish is successfully created when valid data is provided
        """
        # pylint: disable=no-member
        Dish.objects.create(name="Pizza", price=10.5)
        self.assertEqual(Dish.objects.count(), 1)

    def test_name_is_unique(self):
        """
        Verifies that the dish name is unique in the database
        """
        # pylint: disable=no-member
        Dish.objects.create(name="Pizza", description="Tasty", price=10.5)
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                Dish.objects.create(name="Pizza", description="Duplicate", price=12.5)


class TestReservationModel(TestCase):
    """
    TestReservation class
    """

    def test_creates_reservation_when_data_is_valid(self):
        """
        Verifies that a reservation is successfully created when valid data is provided
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
