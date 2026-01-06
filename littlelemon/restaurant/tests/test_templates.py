# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2026-01-05 21:49:45
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2026-01-06 06:00:11
"""
Test Templates
"""
from django.test import TestCase
from django.urls import reverse

from restaurant.models import Dish


class TestTemplate(TestCase):
    """
    TestTemplate class
    """

    def test_templates_used_by_home_url(self):
        """
        Verifies that the home url renders the expected template
        """
        response = self.client.get(reverse("restaurant:home"))
        self.assertTemplateUsed(response, "restaurant/home.html")

    def test_templates_used_by_about_url(self):
        """
        Verifies that the about url renders the expected template
        """
        response = self.client.get(reverse("restaurant:about"))
        self.assertTemplateUsed(response, "restaurant/about.html")

    def test_templates_used_by_menu_url(self):
        """
        Verifies that the menu url renders the expected template
        """
        response = self.client.get(reverse("restaurant:menu"))
        self.assertTemplateUsed(response, "restaurant/menu.html")

    def test_templates_used_by_dish_detail_url(self):
        """
        Tests templates used by dish detail
        """
        # pylint: disable=no-member
        dish = Dish.objects.create(name="Pizza", price=10.5)
        response = self.client.get(
            reverse("restaurant:dish_detail", kwargs={"pk": dish.pk})
        )
        self.assertTemplateUsed(response, "restaurant/dish.html")

    def test_templates_used_by_reserve_table_url(self):
        """
        Verifies that the reserve table url renders the expected template
        """
        response = self.client.get(reverse("restaurant:reserve_table"))
        self.assertTemplateUsed(response, "restaurant/reserve_table.html")

    def test_templates_used_by_opening_hours_url(self):
        """
        Verifies that the opening hours url renders the expected template
        """
        response = self.client.get(reverse("restaurant:opening_hours"))
        self.assertTemplateUsed(response, "restaurant/opening_hours.html")
