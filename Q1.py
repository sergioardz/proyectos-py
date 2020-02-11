#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 14:33:19 2020

@author: sergioardz
"""
import math

def areas(r, a):
    """
    :param r: (float) The radius of the circle.
    :param a: (float) The angle of the segment.
    :returns: (list) (A list of two elements containing the area inside, and area outside the circle, in that order.)
    """
    res = []
    aux = math.pi / 180
    area = math.pi * r ** 2
    segment = (r ** 2 / 2) * (a * aux - math.sin(a * aux))
    outside = area - segment
    res.append(segment)
    res.append(outside)
    return res

print(areas(10, 90));