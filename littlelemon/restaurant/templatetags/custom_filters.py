# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2026-01-04 10:50:03
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2026-01-04 10:52:43
"""
Additional filters for templates
"""
from django import template

register = template.Library()
@register.filter(name="trim")
def trim(value):
    """
    Removes leading and trailing whitespace
    """
    if isinstance(value, str):
        return value.strip()
    return value
