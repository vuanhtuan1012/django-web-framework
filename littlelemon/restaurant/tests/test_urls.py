# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2026-01-03 19:57:40
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2026-01-06 05:48:12
"""
Test URLs
"""
from django.test import TestCase
from django.urls import resolve, reverse

from restaurant.views import (
    AboutView,
    DishDetailView,
    DishListView,
    HomeView,
    OpeningHoursView,
    reserve_table,
)


class TestUrl(TestCase):
    """
    TestUrl class
    """

    def test_home_url_resolves_to_correct_view(self):
        """
        Verifies that the home URL resolves to the correct view
        """
        resolver = resolve(reverse("restaurant:home"))
        self.assertEqual(resolver.func.view_class, HomeView)

    def test_about_url_resolves_to_correct_view(self):
        """
        Verifies that the about URL resolves to the correct view
        """
        resolver = resolve(reverse("restaurant:about"))
        self.assertEqual(resolver.func.view_class, AboutView)

    def test_menu_url_resolves_to_correct_view(self):
        """
        Verifies that the menu URL resolves to the correct view
        """
        resolver = resolve(reverse("restaurant:menu"))
        self.assertEqual(resolver.func.view_class, DishListView)

    def test_dish_detail_url_resolves_to_correct_view(self):
        """
        Tests dish detail url
        """
        resolver = resolve(reverse("restaurant:dish_detail", kwargs={"pk": 1}))
        self.assertEqual(resolver.func.view_class, DishDetailView)

    def test_reserve_table_url_resolves_to_correct_view(self):
        """
        Verifies that the reserve table URL resolves to the correct view
        """
        resolver = resolve(reverse("restaurant:reserve_table"))
        self.assertEqual(resolver.func, reserve_table)

    def test_opening_hours_url_resolves_to_correct_view(self):
        """
        Verifies that the opening hours URL resolves to the correct view
        """
        resolver = resolve(reverse("restaurant:opening_hours"))
        self.assertEqual(resolver.func.view_class, OpeningHoursView)
