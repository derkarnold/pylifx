***************************
Example: Working with bulbs
***************************

Rainbow lights
==============

This script enumerates through bulbs on the network, and sets them to colours across the spectrum, creating a rainbow effect.

.. code-block:: pycon

   >>> import pylifx
   >>> # Connect to the LIFX PAN Gateway (replace with your bulb's MAC)
   >>> controller = pylifx.LifxController('d0:73:d5:00:00:00')

   >>> # Discover bulbs on the PAN
   >>> controller.find_bulbs()
   Getting light state D0:73:D5:00:00:00
   >>> for bulb in controller.bulbs:
   ...    print bulb.bulb_addr, bulb.label
   d073d5000000 Lounge Room
   d073d5000001 Kitchen
   d073d5000002 Master Bedroom
   
   >>> # Set bulbs to a rainbow
   >>> hue_per_bulb = 1.0 / len(controller.bulbs)
   >>> for idx, bulb in enumerate(controller.bulbs):
   ...    bulb.set_hsb(hue_per_bulb * idx, 1, .5)
   >>> controller.on()