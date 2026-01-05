# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2026-01-05 18:47:10
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2026-01-05 21:03:43
"""
Test Views
"""
from django.test import TestCase
from django.urls import reverse

from restaurant.models import Dish


class ViewTest(TestCase):
    """
    ViewTest
    """

    def test_pages_status_code(self):
        """
        Tests pages home, about, menu, reserve table, opening hours status code
        """
        pages = [
            "restaurant:home",
            "restaurant:about",
            "restaurant:menu",
            "restaurant:reserve_table",
            "restaurant:opening_hours",
        ]
        for page in pages:
            with self.subTest(page=page):
                response = self.client.get(reverse(page))
                self.assertEqual(response.status_code, 200)

    def test_dish_detail_status_code(self):
        """
        Test dish detail page status code
        """
        dish = Dish.objects.create(
            name="Pizza", description="Tasty", price=10.5
        )  # pylint: disable=no-member
        response = self.client.get(
            reverse("restaurant:dish_detail", kwargs={"pk": dish.pk})
        )
        self.assertEqual(response.status_code, 200)
