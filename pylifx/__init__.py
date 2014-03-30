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

__all__ = ['networking', 'packet', 'pylifx']
__licence__ = '''
Copyright (c) 2014, Deryck Arnold
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''


from colorsys import rgb_to_hsv
from threading import Lock
from thread import start_new_thread
from networking import LifxBulbTCPServer, LifxUDPSocket, get_interface
from time import sleep

_LIFX_PORT = 56700
_UDP_BROADCAST_ADDR = ('255.255.255.255', _LIFX_PORT)
_RECV_BIND_ADDR = ('0.0.0.0', _LIFX_PORT)
_ONE_SECOND = 10000

def _interpolate(min_x, max_x, min_fx, max_fx, x):
    range_x = max_x - min_x
    return min_fx + (max_fx - min_fx)*(x - min_x)/range_x        

def _smooth_gradient(gradient):
    smoothed_gradient = []
    timings = sorted(gradient.keys())
    for i in range(0, len(timings)-1):
        min_x = timings[i]
        max_x = timings[i+1]
        min_fx = gradient[min_x]
        max_fx = gradient[max_x]
        smoothed_gradient.append(gradient[min_x])
        for x in range(min_x+1, max_x):
            red = _interpolate(min_x, max_x, min_fx[0], max_fx[0], x)
            green = _interpolate(min_x, max_x, min_fx[1], max_fx[1], x)
            blue = _interpolate(min_x, max_x, min_fx[2], max_fx[2], x)
            smoothed_gradient.append((red, green, blue))
        smoothed_gradient.append(gradient[max_x])
    return smoothed_gradient

class LifxController:
    def __init__(self, site_addr, bulb_addr = None, name = None, intf_name = None):
        if site_addr is None:
            raise ValueError('site_addr cannot be None.')
        if name is None:
            self._name = site_addr
        else:
            self._name = name
        net_intf = get_interface(intf_name)
        self._socket = LifxUDPSocket(site_addr, bulb_addr, net_intf, _LIFX_PORT, _LIFX_PORT)
    
    def __enter__(self):
        return self
        
    def __exit__(self, type, value, traceback):
        self.close()
        
    def __del__(self):
        self.close()
    
    def close(self):
        if self._socket is not None:
            self._socket.close()
            self._socket = None
    
    def on(self):
        print 'Turning on', self._name
        self._socket.send_to_bulb('setPowerState', onoff = 0xff)
    
    def off(self):
        print 'Turning off', self._name
        self._socket.send_to_bulb('setPowerState', onoff = 0x00)
        
    def set_rgb(self, red, green, blue, fadeTime = 1):
        print 'Setting colour of %s to (R:%f, G:%f, B:%f) over %d seconds' % (self._name, red, green, blue, fadeTime)
        hue, saturation, brightness = rgb_to_hsv(red, green, blue)
        self._set_colour(hue, saturation, brightness, 0, fadeTime)
    
    def set_hsb(self, hue, saturation, brightness, fadeTime = 1):
        print 'Setting colour of %s to (H:%f, S:%f, B:%f) over %d seconds' % (self._name, hue, saturation, brightness, fadeTime)
        self._set_colour(hue, saturation, brightness, 0, fadeTime)
    
    def set_temperature(self, kelvin, fadeTime = 1):
        print 'Setting colour temperature of %s to (%dK) over %d seconds' % (self._name, kelvin, fadeTime)
        self._set_colour(0, 0, 1.0, kelvin, fadeTime)
    
    def run_scene(self, gradient):
        for red, green, blue in _smooth_gradient(gradient):
            self.set_rgb(red, green, blue, fadeTime = 1)
            sleep(1)    
    
    def _set_colour(self, hue, saturation, brightness, kelvin, fadeTime):
        fadeTime = fadeTime * _ONE_SECOND
        hue = hue * 0xffff
        saturation = saturation * 0xffff
        brightness = brightness * 0xffff
        self._socket.send_to_bulb('setLightColour',
                   stream = 0,
                   hue = hue, saturation = saturation, brightness = brightness,
                   kelvin = kelvin,
                   fadeTime = fadeTime)

class LifxBulbEmulator:
    _properties = {
        'bulbLabel': '\x00' * 32,#'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
        'hue': 0,
        'saturation': 0,
        'brightness': 0xffff,
        'power': 0xffff,
        'onoff': 0xffff,
        'tags': 0,
        'dim': 100,
        'kelvin': 3500,
    }
    
    def __init__(self, site_addr, bulb_addr, intf_name = None):
        self._prop_lock = Lock()
        net_intf = get_interface(intf_name)
        self._tcpsock = LifxBulbTCPServer(net_intf, self._handle_sock, _LIFX_PORT)
        self._udpsock = LifxUDPSocket(site_addr, bulb_addr, net_intf, _LIFX_PORT, _LIFX_PORT)
    
    def __enter__(self):
        return self
        
    def __exit__(self, type, value, traceback):
        self.close()
    
    def __del__(self):
        self.close()
    
    def close(self):
        if self._udpsock is not None:
            self._udpsock.close()
            self._udpsock = None
        if self._tcpsock is not None:
            self._tcpsock.close()
            self._tcpsock = None
    
    def start(self):
        start_new_thread(self._handle_sock, (self._udpsock,))
        self._tcpsock.start()
    
    def _handle_sock(self, lifx_socket):
        try:
            while True:
                ((msg_type, msg_data), addr) = lifx_socket.recv()
                
                if addr is not None and addr[0] == self._tcpsock.net_intf['addr']:
                    continue
                self._msg_recevied(lifx_socket, msg_type, msg_data)
        except Exception as e:
            print 'Exception on', lifx_socket, '-', e
        finally:
            try:
                print 'Closing', lifx_socket
                lifx_socket.close()
            except:
                pass
    
    def _msg_recevied(self, lifx_socket, msg_type, msg_data):
        if msg_type != 'getPanGateway': # too spammy.
            print lifx_socket, msg_type, msg_data
        if msg_type == 'getPanGateway':
            lifx_socket.send_as_bulb('panGateway', service = 2, port = _LIFX_PORT)
            lifx_socket.send_as_bulb('panGateway', service = 1, port = _LIFX_PORT)
        elif msg_type == 'setLightColour':
            self._copy_props(msg_data)
            self._send_light_state(lifx_socket)
        elif msg_type == 'setDimAbsolute':
            with self._prop_lock:
                self._properties['dim'] = msg_type['brightness']
        elif msg_type == 'getLightState':
            self._send_light_state(lifx_socket)
        elif msg_type == 'setPowerState':
            self._copy_props(msg_data)
            self._send_power_state(lifx_socket)
        elif msg_type == 'getPowerState':
            self._send_power_state(lifx_socket)
    
    def _copy_props(self, from_msg):
        with self._prop_lock:
            for key, value in from_msg.items():
                if self._properties.has_key(key):
                    self._properties[key] = value
    
    def _send_light_state(self, sock):
        with self._prop_lock:
            sock.send_as_bulb('lightStatus', **self._properties)
            self._udpsock.send_as_bulb('lightStatus', **self._properties)
            
    def _send_power_state(self, sock ):
        with self._prop_lock:
            sock.send_as_bulb('powerState', **self._properties)
            self._udpsock.send_as_bulb('powerState', **self._properties)
            
class LifxBulbBridge(LifxBulbEmulator):
    _reserved_fields = {
        'bulb_addr',
        'site_addr',
        'protocol',
    }
    def __init__(self, site_addr, bulb_addr, intf_name = None):
        LifxBulbEmulator.__init__(self, site_addr, bulb_addr, intf_name)
        
    def _msg_recevied(self, lifx_socket, msg_type, msg_data):
        LifxBulbEmulator._msg_recevied(self, lifx_socket, msg_type, msg_data)
        if not msg_type.startswith('getPanGateway'):
            new_data = dict([(k, v) for k, v in msg_data.items() if k not in self._reserved_fields])
            self._udpsock.send_to_bulb(msg_type, **new_data)