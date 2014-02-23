#!/bin/python
# -*- coding: utf-8 -*-
"""
@author: Deryck Arnold
"""

def rgbToHsl(red, green, blue):
    r = float(red)
    g = float(green)
    b = float(blue)
    cMax = max(r, g, b)
    cMin = min(r, g, b)
    c = cMax - cMin
    
    if c == 0:
        hue = 0
    elif cMax == r:
        hue = (g - b)/c
    elif cMax == g:
        hue = (b - r)/c + 2
    elif cMax == b:
        hue = (r - g)/c + 4
        
    lightness = (cMax + cMin)/2
    if c == 0:
        saturation = 0
    else:
        saturation = c / (1 - (2*lightness - 1))
        
    return hue / 6.0, saturation, lightness

def rgbToHsb(red, green, blue):
    r = float(red)
    g = float(green)
    b = float(blue)
    cMax = max(r, g, b)
    cMin = min(r, g, b)
    c = cMax - cMin
    
    if c == 0:
        hue = 0
    elif cMax == r:
        hue = (g - b)/c
    elif cMax == g:
        hue = (b - r)/c + 2
    elif cMax == b:
        hue = (r - g)/c + 4
        
    if c == 0:
        saturation = 0
    else:
        saturation = c / cMax
        
    brightness = cMax
        
    return (hue % 6.0) / 6.0, saturation, brightness