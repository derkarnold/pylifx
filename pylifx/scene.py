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

# A scene is a map of <seconds> to <colour>, in the format of (red, green, blue).
# Red, green and blue range from 0.0 to 1.0, where 1.0 is the maximum value.
# When passed to run_scene, these points are interpolated to make a smooth series
# to fade through the colours.
SUNRISE = {
    0:   (0.00, 0.00, 0.00),
    30:  (0.05, 0.00, 0.00),
    90:  (0.20, 0.05, 0.00),
    120: (0.30, 0.15, 0.00),
    150: (0.40, 0.30, 0.00),
    210: (0.50, 0.45, 0.00),
    240: (0.60, 0.55, 0.00),
    270: (0.70, 0.65, 0.10),
    300: (0.80, 0.80, 0.20),
    330: (0.90, 0.90, 0.30),
    360: (1.00, 1.00, 0.40),
    390: (1.00, 1.00, 0.50),
    420: (1.00, 1.00, 0.60),
    450: (1.00, 1.00, 0.70),
    480: (1.00, 1.00, 0.80),
    510: (1.00, 1.00, 0.90),
    540: (1.00, 1.00, 1.00),
}