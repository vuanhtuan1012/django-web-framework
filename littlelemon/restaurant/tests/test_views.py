# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2026-01-05 18:47:10
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2026-01-06 05:59:08
"""
Test Views
"""
from django.test import TestCase
from django.urls import reverse

from restaurant.models import Dish


class TestView(TestCase):
    """
    TestView class
    """

    def test_home_view_returns_200(self):
        """
        Verifies that the home view returns a 200 OK response
        """
        response = self.client.get(reverse("restaurant:home"))
        self.assertEqual(response.status_code, 200)

    def test_about_view_returns_200(self):
        """
        Verifies that the about view returns a 200 OK response
        """
        response = self.client.get(reverse("restaurant:about"))
        self.assertEqual(response.status_code, 200)

    def test_menu_view_returns_200(self):
        """
        Verifies that the menu view returns a 200 OK response
        """
        response = self.client.get(reverse("restaurant:menu"))
        self.assertEqual(response.status_code, 200)

    def test_dish_detail_view_returns_200(self):
        """
        Verifies that the dish detail view returns a 200 OK response
        """
        # pylint: disable=no-member
        dish = Dish.objects.create(name="Pizza", description="Tasty", price=10.5)
        response = self.client.get(
            reverse("restaurant:dish_detail", kwargs={"pk": dish.pk})
        )
        self.assertEqual(response.status_code, 200)

    def test_reseve_table_view_returns_200(self):
        """
        Verifies that the reserve table view returns a 200 OK response
        """
        response = self.client.get(reverse("restaurant:reserve_table"))
        self.assertEqual(response.status_code, 200)

    def test_opening_hours_view_returns_200(self):
        """
        Verifies that the opening hours view returns a 200 OK response
        """
        response = self.client.get(reverse("restaurant:opening_hours"))
        self.assertEqual(response.status_code, 200)
