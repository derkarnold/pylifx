# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 23:08:51 2014

@author: deryck
"""

from lifx import *

addr = 'D0:73:D5:XX:XX:XX'
with LifxBulbBridge(addr, addr, intf_name='eth0') as bridge:
    bridge.start()