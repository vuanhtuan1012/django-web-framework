# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2026-01-03 19:57:40
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2026-01-05 20:38:42
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


class UrlTest(TestCase):
    """
    UrlTest
    """

    def test_urls_resolve_to_correct_views(self):
        """
        Tests home, about, menu, opening hours urls
        """
        test_cases = [
            ("restaurant:home", HomeView),
            ("restaurant:about", AboutView),
            ("restaurant:menu", DishListView),
            ("restaurant:opening_hours", OpeningHoursView),
        ]

        for url_name, view in test_cases:
            with self.subTest(url_name=url_name, view=view):
                resolver = resolve(reverse(url_name))
                self.assertEqual(resolver.func.view_class, view)

    def test_dish_detail_url(self):
        """
        Tests dish detail url
        """
        resolver = resolve(reverse("restaurant:dish_detail", kwargs={"pk": 1}))
        self.assertEqual(resolver.func.view_class, DishDetailView)

    def test_reserve_table_url(self):
        """
        Tests reserve table url
        """
        resolver = resolve(reverse("restaurant:reserve_table"))
        self.assertEqual(resolver.func, reserve_table)
