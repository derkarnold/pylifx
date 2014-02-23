# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 20:23:08 2014

@author: Deryck Arnold

Huge thanks to Kevin Bowman(magicmonkey) and others for the lifxjs project on GitHub:
    https://github.com/magicmonkey/lifxjs/

Without their work on the lifxjs project, this one would not have been possible.
"""

_PACKET_TYPE_OFFSET = 256
_PACKET_TYPE_SIZE = 16
_PACKET_TYPE_SPEC = 'uintle:' + str(_PACKET_TYPE_SIZE)
_HEADER_SPEC = [
    ('packet_size', 'uintle:16'),
    ('protocol', 'uintle:16'),
    ('reserved1', 'pad:32'),
    ('bulb_addr', 'hex:48'),
    ('reserved2', 'pad:16'),
    ('site_addr', 'hex:48'),
    ('reserved3', 'pad:16'),
    ('timestamp', 'uintbe:64'),
    ('packet_type', _PACKET_TYPE_SPEC),
    ('reserved4', 'pad:16'),
]
_HEADER_SIZE = 36

_PAYLOADS = {
    'setDimAbsolute': {
        'packet_type': 0x68,
        'payload_size': 6,
        'payload_spec': [
            ('brightness', 'uintle:16'),
            ('duration', 'uintbe:32'),
        ],
    },
    'setDimRelative': {
        'packet_type': 0x69,
        'payload_size': 6,
        'payload_spec': [
            ('brightness', 'uintle:16'),
            ('duration', 'uintbe:32'),
        ],
    },
    'setLightColour': {
        'packet_type': 0x66,
        'payload_size': 13,
        'payload_spec': [
            ('stream', 'uintbe:8'),
            ('hue', 'uintle:16'),
            ('saturation', 'uintle:16'),
            ('brightness', 'uintle:16'),
            ('kelvin', 'uintle:16'),
            ('fadeTime', 'uintle:32'),
        ],
    },
    'setWaveform': {
        'packet_type': 0x67,
        'payload_size': 21,
        'payload_spec': [
            ('stream', 'uintbe:8'),
            ('transient', 'uintbe:8'),
            ('hue', 'uintle:16'),
            ('saturation', 'uintle:16'),
            ('brightness', 'uintle:16'),
            ('kelvin', 'uintle:16'),
            ('period', 'uintle:32'),
            ('cycles', 'floatbe'),
            ('dutyCycles', 'uintbe:16'),
            ('waveform', 'uintbe:8'),
        ],
    },
    'getLightState': {
        'packet_type': 0x65,
        'payload_size': 0,
        'payload_spec': [

        ],
    },
    'disableFactoryTestMode': {
        'packet_type': 0x28,
        'payload_size': 0,
        'payload_spec': [

        ],
    },
    'getInfo': {
        'packet_type': 0x22,
        'payload_size': 0,
        'payload_spec': [

        ],
    },
    'infoState': {
        'packet_type': 0x23,
        'payload_size': 24,
        'payload_spec': [
            ('time', 'uintle:64'),
            ('uptime', 'uintle:64'),
            ('downtime', 'uintle:64'),
        ],
    },
    'getVersion': {
        'packet_type': 0x20,
        'payload_size': 0,
        'payload_spec': [

        ],
    },
    'versionState': {
        'packet_type': 0x21,
        'payload_size': 12,
        'payload_spec': [
            ('vendor', 'uintbe:32'),
            ('product', 'uintbe:32'),
            ('version', 'uintbe:32'),
        ],
    },
    'reboot': {
        'packet_type': 0x26,
        'payload_size': 0,
        'payload_spec': [

        ],
    },
    'setFactoryTestMode': {
        'packet_type': 0x27,
        'payload_size': 1,
        'payload_spec': [
            ('on', 'uintbe:8'),
        ],
    },
    'getMcuRailVoltage': {
        'packet_type': 0x24,
        'payload_size': 0,
        'payload_spec': [

        ],
    },
    'mcuRailVoltage': {
        'packet_type': 0x25,
        'payload_size': 4,
        'payload_spec': [
            ('voltage', 'uintle:32'),
        ],
    },
    'lightStatus': {
        'packet_type': 0x6b,
        'payload_size': 52,
        'payload_spec': [
            ('hue', 'uintle:16'),
            ('saturation', 'uintle:16'),
            ('brightness', 'uintle:16'),
            ('kelvin', 'uintle:16'),
            ('dim', 'uintle:16'),
            ('power', 'uintle:16'),
            ('bulbLabel', 'bytes:32'),
            ('tags', 'uintbe:64'),
        ],
    },
    'setAccessPoints': {
        'packet_type': 0x131,
        'payload_size': 98,
        'payload_spec': [
            ('interface', 'uintbe:8'),
            ('ssid', 'bytes:32'),
            ('password', 'bytes:64'),
            ('securityProtocol', 'uintbe:8'),
        ],
    },
    'getAccessPoints': {
        'packet_type': 0x130,
        'payload_size': 0,
        'payload_spec': [

        ],
    },
    'accessPoint': {
        'packet_type': 0x132,
        'payload_size': 38,
        'payload_spec': [
            ('interface', 'uintbe:8'),
            ('ssid', 'bytes:32'),
            ('securityProtocol', 'uintbe:8'),
            ('strength', 'uintbe:16'),
            ('channel', 'uintbe:16'),
        ],
    },
    'wifiState': {
        'packet_type': 0x12f,
        'payload_size': 22,
        'payload_spec': [
            ('interface', 'uintbe:8'),
            ('wifiStatus', 'uintbe:8'),
            ('ip4Address', 'hex:32'),
            ('ip6Address', 'hex:128'),
        ],
    },
    'getWifiState': {
        'packet_type': 0x12d,
        'payload_size': 1,
        'payload_spec': [
            ('interface', 'uintbe:8'),
        ],
    },
    'setWifiState': {
        'packet_type': 0x12e,
        'payload_size': 22,
        'payload_spec': [
            ('interface', 'uintbe:8'),
            ('wifiStatus', 'uintbe:8'),
            ('ip4Address', 'hex:32'),
            ('ip6Address', 'hex:128'),
        ],
    },
    'resetSwitchState': {
        'packet_type': 0x08,
        'payload_size': 2,
        'payload_spec': [
            ('position', 'uintbe:8'),
        ],
    },
    'getTime': {
        'packet_type': 0x04,
        'payload_size': 0,
        'payload_spec': [

        ],
    },
    'setTime': {
        'packet_type': 0x05,
        'payload_size': 8,
        'payload_spec': [
            ('time', 'uintle:64'),
        ],
    },
    'timeState': {
        'packet_type': 0x06,
        'payload_size': 8,
        'payload_spec': [
            ('time', 'uintle:64'),
        ],
    },
    'getResetSwitchState': {
        'packet_type': 0x07,
        'payload_size': 0,
        'payload_spec': [

        ],
    },
    'getPanGateway': {
        'packet_type': 0x02,
        'payload_size': 0,
        'payload_spec': [

        ],
    },
    'panGateway': {
        'packet_type': 0x03,
        'payload_size': 5,
        'payload_spec': [
            ('service', 'uintbe:8'),
            ('port', 'uintle:32'),
        ],
    },
    'tagLabels': {
        'packet_type': 0x1f,
        'payload_size': 40,
        'payload_spec': [
            ('tags', 'uintbe:64'),
            ('label', 'bytes:32'),
        ],
    },
    'setTagLabels': {
        'packet_type': 0x1e,
        'payload_size': 40,
        'payload_spec': [
            ('tags', 'uintbe:64'),
            ('label', 'bytes:32'),
        ],
    },
    'getTagLabels': {
        'packet_type': 0x1d,
        'payload_size': 8,
        'payload_spec': [
            ('tags', 'uintbe:64'),
        ],
    },
    'tags': {
        'packet_type': 0x1c,
        'payload_size': 8,
        'payload_spec': [
            ('tags', 'uintbe:64'),
        ],
    },
    'setTags': {
        'packet_type': 0x1b,
        'payload_size': 8,
        'payload_spec': [
            ('tags', 'uintbe:64'),
        ],
    },
    'getTags': {
        'packet_type': 0x1a,
        'payload_size': 0,
        'payload_spec': [

        ],
    },
    'bulbLabel': {
        'packet_type': 0x19,
        'payload_size': 32,
        'payload_spec': [
            ('label', 'bytes:32'),
        ],
    },
    'setBulbLabel': {
        'packet_type': 0x18,
        'payload_size': 32,
        'payload_spec': [
            ('label', 'bytes:32'),
        ],
    },
    'getBulbLabel': {
        'packet_type': 0x17,
        'payload_size': 0,
        'payload_spec': [

        ],
    },
    'powerState': {
        'packet_type': 0x16,
        'payload_size': 2,
        'payload_spec': [
            ('onoff', 'uintbe:16'),
        ],
    },
    'setPowerState': {
        'packet_type': 0x15,
        'payload_size': 2,
        'payload_spec': [
            ('onoff', 'uintbe:16'),
        ],
    },
    'getPowerState': {
        'packet_type': 0x14,
        'payload_size': 0,
        'payload_spec': [

        ],
    },
    'wifiFirmwareState': {
        'packet_type': 0x13,
        'payload_size': 20,
        'payload_spec': [
            ('build_second', 'uintbe:8'),
            ('build_minute', 'uintbe:8'),
            ('build_hour', 'uintbe:8'),
            ('build_day', 'uintbe:8'),
            ('build_month', 'bytes:3'),
            ('build_year', 'uintbe:8'),
            ('install_second', 'uintbe:8'),
            ('install_minute', 'uintbe:8'),
            ('install_hour', 'uintbe:8'),
            ('install_day', 'uintbe:8'),
            ('install_month', 'bytes:3'),
            ('install_year', 'uintbe:8'),
            ('version', 'uintle:32'),
        ],
    },
    'getWifiFirmwareState': {
        'packet_type': 0x12,
        'payload_size': 0,
        'payload_spec': [

        ],
    },
    'wifiInfo': {
        'packet_type': 0x11,
        'payload_size': 14,
        'payload_spec': [
            ('signal', 'floatle'),
            ('tx', 'uintle:32'),
            ('rx', 'uintle:32'),
            ('mcuTemperature', 'uintbe:16'),
        ],
    },
    'getWifiInfo': {
        'packet_type': 0x10,
        'payload_size': 0,
        'payload_spec': [

        ],
    },
    'meshInfo': {
        'packet_type': 0x0d,
        'payload_size': 14,
        'payload_spec': [
            ('signal', 'floatle'),
            ('tx', 'uintle:32'),
            ('rx', 'uintle:32'),
            ('mcuTemperature', 'uintbe:16'),
        ],
    },
    'getMeshFirmware': {
        'packet_type': 0x0e,
        'payload_size': 0,
        'payload_spec': [

        ],
    },
    'meshFirmware': {
        'packet_type': 0x0f,
        'payload_size': 20,
        'payload_spec': [
            ('build_second', 'uintbe:8'),
            ('build_minute', 'uintbe:8'),
            ('build_hour', 'uintbe:8'),
            ('build_day', 'uintbe:8'),
            ('build_month', 'bytes:3'),
            ('build_year', 'uintbe:8'),
            ('install_second', 'uintbe:8'),
            ('install_minute', 'uintbe:8'),
            ('install_hour', 'uintbe:8'),
            ('install_day', 'uintbe:8'),
            ('install_month', 'bytes:3'),
            ('install_year', 'uintbe:8'),
            ('version', 'uintle:32'),
        ],
    },
    'getMeshInfo': {
        'packet_type': 0x0c,
        'payload_size': 0,
        'payload_spec': [

        ],
    },
}

_PACK_SPECS = {} # Dict of name -> format for bitstring.pack
_READ_SPECS = {} # Dict of packet_type -> (format for bitstring.readlist, field names, name)

def _processForPack(payload_spec, packet_type, payload_size):
    named_types = [
        t + '=' + ('0' if t.startswith('pad:') else n)
        for n, t in payload_spec
    ]
    fmt_str = ', '.join(named_types) \
        .replace('timestamp', '0') \
        .replace('packet_size', str(_HEADER_SIZE + payload_size)) \
        .replace('packet_type', str(packet_type))
    return fmt_str

def _processForRead(payload_name, payload_spec):
    type_format = ', '.join([t for _, t in payload_spec])
    fields = [n for n, t in payload_spec if not t.startswith('pad:')]
    return {
        'name': payload_name,
        'format': type_format,
        'fields': fields, 
    }

for name, values in _PAYLOADS.items():
    combined_spec = _HEADER_SPEC + values['payload_spec']
    _PACK_SPECS[name] = _processForPack(combined_spec, values['packet_type'], values['payload_size'])
    _READ_SPECS[values['packet_type']] = _processForRead(name, combined_spec)

from bitstring import pack, ConstBitStream

def encode(packet_name, **kwargs):
    spec = _PACK_SPECS[packet_name]
    packet = pack(spec, **kwargs)
    return packet

def decode(byte_string):
    data = ConstBitStream(bytes=byte_string)
    packet_type = data[_PACKET_TYPE_OFFSET:_PACKET_TYPE_OFFSET+_PACKET_TYPE_SIZE].read(_PACKET_TYPE_SPEC)
    read_spec = _READ_SPECS[packet_type]
    values = data.readlist(read_spec['format'])
    return read_spec['name'], dict(zip(read_spec['fields'], values))