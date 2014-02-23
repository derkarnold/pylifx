#!/bin/python
# -*- coding: utf-8 -*-
"""
@author: Deryck Arnold
"""

from socket import socket, AF_INET, SOCK_DGRAM, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR, SO_BROADCAST
from packet import encode, decode
from re import match
from thread import start_new_thread
from netifaces import ifaddresses, interfaces

_RECV_BUFFER_SIZE = 1024
_LIFX_PROTO_TOBULB = 13312
_LIFX_PROTO_ASBULB = 21504
_BLANK_MAC = '00:00:00:00:00:00'
_MAC_ADDR_FORMAT = '([A-z0-9]{2})[:\-]([A-z0-9]{2})[:\-]([A-z0-9]{2})[:\-]([A-z0-9]{2})[:\-]([A-z0-9]{2})[:\-]([A-z0-9]{2})'
_AVAILABLE_INTERFACES = {}

# Only support IPv4. Broadcast isn't in IPv6.
for intf_name in interfaces():
    addrs = ifaddresses(intf_name)
    if addrs.has_key(AF_INET):
        _AVAILABLE_INTERFACES[intf_name] = addrs[AF_INET][0]

def get_interfaces():
    return _AVAILABLE_INTERFACES

def get_interface(intf_name):
    if intf_name is None:
        return _AVAILABLE_INTERFACES.itervalues().next()
    else:
        return _AVAILABLE_INTERFACES[intf_name]

def _processMAC(mac):
    if mac is None:
        mac = _BLANK_MAC
    m = match(_MAC_ADDR_FORMAT, mac)
    if m is None:
        raise ValueError('invalid MAC address:', mac, '. Address must be colon or hyphen delimited.')
    else:
        return ''.join(m.groups())

class LifxSocket:
    def __init__(self, site_addr, bulb_addr, sock, net_addr):
        self._site_addr = _processMAC(site_addr)
        self._bulb_addr = _processMAC(bulb_addr)
        self._socket = sock
        self._net_addr = net_addr
        
    def __del__(self):
        self.close()
    
    def __str__(self):
        return str(self._net_addr)
    
    def __repr__(self):
        return self.__str__()    
    
    def close(self):
        if self._socket is not None:
            self._socket.close()
            self._socket = None
    
    def send_to_bulb(self, packet_name, **kwargs):
        self._send(_LIFX_PROTO_TOBULB, packet_name, kwargs)
    
    def send_as_bulb(self, packet_name, **kwargs):
        self._send(_LIFX_PROTO_ASBULB, packet_name, kwargs)
        
    def recv(self):
        while True:
            raw_data, addr = self._socket.recvfrom(_RECV_BUFFER_SIZE)
            if raw_data == None or len(raw_data) == 0:
                raise IOError('disconnected')
            try:
                return decode(raw_data), addr
            except Exception as e:
                print 'Invalid packet from', self._net_addr, '-', e
    
    def _send(self, protocol, packet_name, kwargs):
        packet = encode(packet_name,
                        protocol = protocol,
                        site_addr = self._site_addr,
                        bulb_addr = self._bulb_addr,
                        **kwargs)
        self._send_raw(packet)
    
    def _send_raw(self, packet):
        if self._socket is None:
            raise IOError('socket is closed.')
        else:
            self._socket.sendto(packet.bytes, self._net_addr)

class LifxUDPSocket(LifxSocket):
    def __init__(self, site_addr, bulb_addr, net_intf, send_port, bind_port):
        sock = socket(AF_INET, SOCK_DGRAM)
        sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
        if bind_port is not None:
            sock.bind(('', bind_port))
        LifxSocket.__init__(self, site_addr, bulb_addr, sock, (net_intf['broadcast'], send_port))

class LifxBulbTCPServer:
    def __init__(self, net_intf, handle_func, bind_port):
        self.net_intf = net_intf
        self._bind_addr = (net_intf['addr'], bind_port)
        self._handle_func = handle_func
        self._socket = socket(AF_INET, SOCK_STREAM)
        self._socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self._socket.bind(self._bind_addr)
    
    def __del__(self):
        self.close()
        
    def close(self):
        if self._socket is not None:
            self._socket.close()
            self._socket = None
    
    def start(self):
        self._socket.listen(1)
        while True:
            sock, addr = self._socket.accept()
            print 'New TCP connection on', str(self._bind_addr) + ':', addr
            lifx_socket = LifxSocket(None, None, sock, addr)
            start_new_thread(self._handle_func, (lifx_socket,))