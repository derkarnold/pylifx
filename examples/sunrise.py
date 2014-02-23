# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 19:29:47 2014

@author: deryck
"""

from lifx import LifxController
import scene

addr = 'D0:73:D5:XX:XX:XX'
with LifxController(addr) as bulb:
	bulb.on()
    bulb.run_scene(scene.SUNRISE)