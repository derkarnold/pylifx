#!/bin/python
# -*- coding: utf-8 -*-
"""
@author: Deryck Arnold
"""

from pylifx import LifxBulbBridge

addr = 'D0:73:D5:XX:XX:XX'
with LifxBulbBridge(addr, addr) as bridge:
    bridge.start()