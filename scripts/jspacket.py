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

Huge thanks to Kevin Bowman(magicmonkey) and others for the lifxjs project on GitHub:
    https://github.com/magicmonkey/lifxjs/

Without their work on the lifxjs project, this one would not have been possible.
"""

js_spec = '''{
	0x02: {
		name:"Get PAN gateway",
		shortname:"getPanGateway",
		length:0,
		fields:[]
	},
	0x03: {
		name:"PAN gateway",
		shortname:"panGateway",
		length:5,
		fields:[
			{name:"service", type:type.uint8}    ,
			{name:"port"   , type:type.uint32_le}
		]
	},
	0x04: {
		name:"Get time",
		shortname:"getTime",
		length:0,
		fields:[]
	},
	0x05: {
		name:"Set time",
		shortname:"setTime",
		length:8,
		fields:[
			{name:"time", type:type.uint64_le}
		]
	},
	0x06: {
		name:"Time state",
		shortname:"timeState",
		length:8,
		fields:[
			{name:"time", type:type.uint64_le}
		]
	},
	0x07: {
		name:"Get reset switch state",
		shortname:"getResetSwitchState",
		length:0,
		fields:[]
	},
	0x08: {
		name:"Reset switch state",
		shortname:"resetSwitchState",
		length:2,
		fields:[
			{name:"position", type:type.uint8}
		]
	},
	0x0c: {
		name:"Get mesh info",
		shortname:"getMeshInfo",
		length:0,
		fields:[]
	},
	0x0d: {
		name:"Mesh info",
		shortname:"meshInfo",
		length:14,
		fields:[
			{name:"signal"        , type:type.float_le} ,
			{name:"tx"            , type:type.uint32_le},
			{name:"rx"            , type:type.uint32_le},
			{name:"mcuTemperature", type:type.uint16}
		]
	},
	0x0e: {
		name:"Get mesh firmware",
		shortname:"getMeshFirmware",
		length:0,
		fields:[]
	},
	0x0f: {
		name:"Mesh firmware",
		shortname:"meshFirmware",
		length:20,
		fields:[
			{name:"build_second"  , type:type.uint8},
			{name:"build_minute"  , type:type.uint8},
			{name:"build_hour"    , type:type.uint8},
			{name:"build_day"     , type:type.uint8},
			{name:"build_month"   , type:type.string3_le},
			{name:"build_year"    , type:type.uint8},
			{name:"install_second", type:type.uint8},
			{name:"install_minute", type:type.uint8},
			{name:"install_hour"  , type:type.uint8},
			{name:"install_day"   , type:type.uint8},
			{name:"install_month" , type:type.string3_le},
			{name:"install_year"  , type:type.uint8},
			{name:"version"       , type:type.uint32_le}
		]
	},
	0x10: {
		name:"Get wifi info",
		shortname:"getWifiInfo",
		length:0,
		fields:[]
	},
	0x11: {
		name:"Wifi info",
		shortname:"wifiInfo",
		length:14,
		fields:[
			{name:"signal"        , type:type.float_le} ,
			{name:"tx"            , type:type.uint32_le},
			{name:"rx"            , type:type.uint32_le},
			{name:"mcuTemperature", type:type.uint16}
		]
	},
	0x12: {
		name:"Get wifi firmware state",
		shortname:"getWifiFirmwareState",
		length:0,
		fields:[]
	},
	0x13: {
		name:"Wifi firmware state",
		shortname:"wifiFirmwareState",
		length:20,
		fields:[
			{name:"build_second"  , type:type.uint8},
			{name:"build_minute"  , type:type.uint8},
			{name:"build_hour"    , type:type.uint8},
			{name:"build_day"     , type:type.uint8},
			{name:"build_month"   , type:type.string3_le},
			{name:"build_year"    , type:type.uint8},
			{name:"install_second", type:type.uint8},
			{name:"install_minute", type:type.uint8},
			{name:"install_hour"  , type:type.uint8},
			{name:"install_day"   , type:type.uint8},
			{name:"install_month" , type:type.string3_le},
			{name:"install_year"  , type:type.uint8},
			{name:"version"       , type:type.uint32_le}
		]
	},
	0x14: {
		name:"Get power state",
		shortname:"getPowerState",
		length:0,
		fields:[]
	},
	0x15: {
		name:"Set power state",
		shortname:"setPowerState",
		length:2,
		fields:[
			{name:"onoff", type:type.uint16},
		]
	},
	0x16: {
		name:"Power state",
		shortname:"powerState",
		length:2,
		fields:[
			{name:"onoff", type:type.uint16},
		]
	},
	0x17: {
		name:"Get bulb label",
		shortname:"getBulbLabel",
		length:0,
		fields:[]
	},
	0x18: {
		name:"Set bulb label",
		shortname:"setBulbLabel",
		length:32,
		fields:[
			{name:"label", type:type.string32},
		]
	},
	0x19: {
		name:"Bulb label",
		shortname:"bulbLabel",
		length:32,
		fields:[
			{name:"label", type:type.string32},
		]
	},
	0x1a: {
		name:"Get tags",
		shortname:"getTags",
		length:0,
		fields:[]
	},
	0x1b: {
		name:"Set tags",
		shortname:"setTags",
		length:8,
		fields:[
			{name:"tags", type:type.uint64},
		]
	},
	0x1c: {
		name:"Tags",
		shortname:"tags",
		length:8,
		fields:[
			{name:"tags", type:type.uint64},
		]
	},
	0x1d: {
		name:"Get tag labels",
		shortname:"getTagLabels",
		length:8,
		fields:[
			{name:"tags", type:type.uint64},
		]
	},
	0x1e: {
		name:"Set tag labels",
		shortname:"setTagLabels",
		length:40,
		fields:[
			{name:"tags", type:type.uint64},
			{name:"label", type:type.string32},
		]
	},
	0x1f: {
		name:"Tag labels",
		shortname:"tagLabels",
		length:40,
		fields:[
			{name:"tags", type:type.uint64},
			{name:"label", type:type.string32},
		]
	},
	0x20: {
		name:"Get version",
		shortname:"getVersion",
		length:0,
		fields:[]
	},
	0x21: {
		name:"Version state",
		shortname:"versionState",
		length:12,
		fields:[
			{name:"vendor",  type:type.uint32},
			{name:"product", type:type.uint32},
			{name:"version", type:type.uint32}
		]
	},
	0x22: {
		name:"Get info",
		shortname:"getInfo",
		length:0,
		fields:[]
	},
	0x23: {
		name:"Info state",
		shortname:"infoState",
		length:24,
		fields:[
			{name:"time"    , type:type.uint64_le},
			{name:"uptime"  , type:type.uint64_le},
			{name:"downtime", type:type.uint64_le}
		]
	},
	0x24: {
		name:"Get MCU rail voltage",
		shortname:"getMcuRailVoltage",
		length:0,
		fields:[]
	},
	0x25: {
		name:"MCU rail voltage",
		shortname:"mcuRailVoltage",
		length:4,
		fields:[
			{name:"voltage", type:type.uint32_le},
		]
	},
	0x26: {
		name:"Reboot",
		shortname:"reboot",
		length:0,
		fields:[]
	},
	0x27: {
		name:"Set factory test mode",
		shortname:"setFactoryTestMode",
		length:1,
		fields:[
			{name:"on", type:type.uint8},
		]
	},
	0x28: {
		name:"Disable factory test mode",
		shortname:"disableFactoryTestMode",
		length:0,
		fields:[]
	},
	0x65: {
		name:"Get light state",
		shortname:"getLightState",
		length:0,
		fields:[]
	},
	0x66: {
		name:"Set light colour",
		shortname:"setLightColour",
		length:13,
		fields:[
			{name:"stream"    , type:type.uint8}    ,
			{name:"hue"       , type:type.uint16_le},
			{name:"saturation", type:type.uint16_le},
			{name:"brightness", type:type.uint16_le},
			{name:"kelvin"    , type:type.uint16_le},
			{name:"fadeTime"  , type:type.uint32_le},
		]
	},
	0x67: {
		name:"Set waveform",
		shortname:"setWaveform",
		length:21,
		fields:[
			{name:"stream"    , type:type.uint8}    ,
			{name:"transient" , type:type.uint8}    ,
			{name:"hue"       , type:type.uint16_le},
			{name:"saturation", type:type.uint16_le},
			{name:"brightness", type:type.uint16_le},
			{name:"kelvin"    , type:type.uint16_le},
			{name:"period"    , type:type.uint32_le},
			{name:"cycles"    , type:type.float}    ,
			{name:"dutyCycles", type:type.uint16}   ,
			{name:"waveform"  , type:type.uint8}    ,
		]
	},
	0x68: {
		name:"Set dim (absolute)",
		shortname:"setDimAbsolute",
		length:6,
		fields:[
			{name:"brightness", type:type.uint16_le},
			{name:"duration"  , type:type.uint32}   ,
		]
	},
	0x69: {
		name:"Set dim (relative)",
		shortname:"setDimRelative",
		length:6,
		fields:[
			{name:"brightness", type:type.uint16_le},
			{name:"duration"  , type:type.uint32}   ,
		]
	},
	0x6b: {
		name:"Light status",
		shortname:"lightStatus",
		length:52,
		fields:[
			{name:"hue"       , type:type.uint16_le},
			{name:"saturation", type:type.uint16_le},
			{name:"brightness", type:type.uint16_le},
			{name:"kelvin"    , type:type.uint16_le},
			{name:"dim"       , type:type.uint16_le},
			{name:"power"     , type:type.uint16_le},
			{name:"bulbLabel" , type:type.string32} ,
			{name:"tags"      , type:type.uint64}   ,
		]
	},
	0x12d: {
		name:"Get wifi state",
		shortname:"getWifiState",
		length:1,
		fields:[
			{name:"interface", type:type.uint8},
		]
	},
	0x12e: {
		name:"Set wifi state",
		shortname:"setWifiState",
		length:22,
		fields:[
			{name:"interface", type:type.uint8},
			{name:"wifiStatus", type:type.uint8},
			{name:"ip4Address", type:type.byte4},
			{name:"ip6Address", type:type.byte16},
		]
	},
	0x12f: {
		name:"Wifi state",
		shortname:"wifiState",
		length:22,
		fields:[
			{name:"interface" , type:type.uint8} ,
			{name:"wifiStatus", type:type.uint8} ,
			{name:"ip4Address", type:type.byte4} ,
			{name:"ip6Address", type:type.byte16},
		]
	},
	0x130: {
		name:"Get access points",
		shortname:"getAccessPoints",
		length:0,
		fields:[]
	},
	0x131: {
		name:"Set access point",
		shortname:"setAccessPoints",
		length:98,
		fields:[
			{name:"interface"       , type:type.uint8}   ,
			{name:"ssid"            , type:type.string32},
			{name:"password"        , type:type.string64},
			{name:"securityProtocol", type:type.uint8}   ,
		]
	},
	0x132: {
		name:"Access point",
		shortname:"accessPoint",
		length:38,
		fields:[
			{name:"interface"       , type:type.uint8}   ,
			{name:"ssid"            , type:type.string32},
			{name:"securityProtocol", type:type.uint8}   ,
			{name:"strength"        , type:type.uint16}  ,
			{name:"channel"         , type:type.uint16}  ,
		]
	},
}'''

import re
js_spec = re.sub(r'([A-z0-9]+):', r'"\1":', js_spec)
field_replacements = {
    'type.uint8': '"uintbe:8"',
    'type.uint16': '"uintbe:16"',
    'type.uint32': '"uintbe:32"',
    'type.uint64': '"uintbe:64"',
    'type.uint8_le': '"uintle:8"',
    'type.uint16_le': '"uintle:16"',
    'type.uint32_le': '"uintle:32"',
    'type.uint64_le': '"uintle:64"',
    'type.float_le': '"floatle"',
    'type.float': '"floatbe"',
    'type.string3_le': '"bytes:3"',
    'type.string32': '"bytes:32"',
    'type.string64': '"bytes:64"',
    'type.byte4': '"hex:32"',
    'type.byte16': '"hex:128"',
}
pattern = re.compile(r'\b(' + '|'.join(field_replacements.keys()) + r')\b')
js_spec = pattern.sub(lambda x: field_replacements[x.group()], js_spec)
js_spec = eval(js_spec)

fmt = '''    '%s': {
        'packet_type': %s,
        'payload_size': %d,
        'payload_spec': [
%s
        ],
    },'''

for packet_type, values in js_spec.items():
    fields = '\r\n'.join(['            (\'%s\', \'%s\'),' % (v['name'], v['type']) for v in values['fields']])
    print fmt % (values['shortname'], packet_type, values['length'], fields)
    