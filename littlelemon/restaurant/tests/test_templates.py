# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2026-01-05 21:49:45
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2026-01-05 22:00:59
"""
Test Templates
"""
from django.test import TestCase
from django.urls import reverse

from restaurant.models import Dish


class TemplateTest(TestCase):
    """
    TemplateTest
    """

    def test_templates_used(self):
        """
        Tests templates used by home, about, menu, reserve table, opening hours
        """
        test_cases = [
            ("restaurant:home", "restaurant/home.html"),
            ("restaurant:about", "restaurant/about.html"),
            ("restaurant:menu", "restaurant/menu.html"),
            ("restaurant:reserve_table", "restaurant/reserve_table.html"),
            ("restaurant:opening_hours", "restaurant/opening_hours.html"),
        ]
        for url_name, template in test_cases:
            with self.subTest(url_name=url_name, template=template):
                response = self.client.get(reverse(url_name))
                self.assertTemplateUsed(response, template)

    def test_dish_detail_template_used(self):
        """
        Tests templates used by dish detail
        """
        instance = Dish.objects.create(
            name="Pizza", price=10.5
        )  # pylint: disable=no-member
        response = self.client.get(
            reverse("restaurant:dish_detail", kwargs={"pk": instance.pk})
        )
        self.assertTemplateUsed(response, "restaurant/dish.html")
