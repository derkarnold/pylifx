#!/bin/python
# -*- coding: utf-8 -*-
"""
@author: Deryck Arnold
"""

from pylifx import LifxController
import pylifx.scene as scene

addr = 'D0:73:D5:XX:XX:XX'
with LifxController(addr) as bulb:
    bulb.on()
    bulb.run_scene(scene.SUNRISE)