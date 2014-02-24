#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author: Deryck Arnold

Copyright (c) 2014, Deryck Arnold
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
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