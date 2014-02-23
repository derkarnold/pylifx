#!/bin/python
# -*- coding: utf-8 -*-
"""
@author: Deryck Arnold
"""

__all__ = ['colour', 'networking', 'packet', 'pylifx']
__licence__ = '''
License

THE WORK (AS DEFINED BELOW) IS PROVIDED UNDER THE TERMS OF THIS CREATIVE COMMONS PUBLIC LICENSE ("CCPL" OR "LICENSE"). THE WORK IS PROTECTED BY COPYRIGHT AND/OR OTHER APPLICABLE LAW. ANY USE OF THE WORK OTHER THAN AS AUTHORIZED UNDER THIS LICENSE OR COPYRIGHT LAW IS PROHIBITED.

BY EXERCISING ANY RIGHTS TO THE WORK PROVIDED HERE, YOU ACCEPT AND AGREE TO BE BOUND BY THE TERMS OF THIS LICENSE. TO THE EXTENT THIS LICENSE MAY BE CONSIDERED TO BE A CONTRACT, THE LICENSOR GRANTS YOU THE RIGHTS CONTAINED HERE IN CONSIDERATION OF YOUR ACCEPTANCE OF SUCH TERMS AND CONDITIONS.

1. Definitions

"Adaptation" means a work based upon the Work, or upon the Work and other pre-existing works, such as a translation, adaptation, derivative work, arrangement of music or other alterations of a literary or artistic work, or phonogram or performance and includes cinematographic adaptations or any other form in which the Work may be recast, transformed, or adapted including in any form recognizably derived from the original, except that a work that constitutes a Collection will not be considered an Adaptation for the purpose of this License. For the avoidance of doubt, where the Work is a musical work, performance or phonogram, the synchronization of the Work in timed-relation with a moving image ("synching") will be considered an Adaptation for the purpose of this License.
"Collection" means a collection of literary or artistic works, such as encyclopedias and anthologies, or performances, phonograms or broadcasts, or other works or subject matter other than works listed in Section 1(f) below, which, by reason of the selection and arrangement of their contents, constitute intellectual creations, in which the Work is included in its entirety in unmodified form along with one or more other contributions, each constituting separate and independent works in themselves, which together are assembled into a collective whole. A work that constitutes a Collection will not be considered an Adaptation (as defined above) for the purposes of this License.
"Distribute" means to make available to the public the original and copies of the Work or Adaptation, as appropriate, through sale or other transfer of ownership.
"Licensor" means the individual, individuals, entity or entities that offer(s) the Work under the terms of this License.
"Original Author" means, in the case of a literary or artistic work, the individual, individuals, entity or entities who created the Work or if no individual or entity can be identified, the publisher; and in addition (i) in the case of a performance the actors, singers, musicians, dancers, and other persons who act, sing, deliver, declaim, play in, interpret or otherwise perform literary or artistic works or expressions of folklore; (ii) in the case of a phonogram the producer being the person or legal entity who first fixes the sounds of a performance or other sounds; and, (iii) in the case of broadcasts, the organization that transmits the broadcast.
"Work" means the literary and/or artistic work offered under the terms of this License including without limitation any production in the literary, scientific and artistic domain, whatever may be the mode or form of its expression including digital form, such as a book, pamphlet and other writing; a lecture, address, sermon or other work of the same nature; a dramatic or dramatico-musical work; a choreographic work or entertainment in dumb show; a musical composition with or without words; a cinematographic work to which are assimilated works expressed by a process analogous to cinematography; a work of drawing, painting, architecture, sculpture, engraving or lithography; a photographic work to which are assimilated works expressed by a process analogous to photography; a work of applied art; an illustration, map, plan, sketch or three-dimensional work relative to geography, topography, architecture or science; a performance; a broadcast; a phonogram; a compilation of data to the extent it is protected as a copyrightable work; or a work performed by a variety or circus performer to the extent it is not otherwise considered a literary or artistic work.
"You" means an individual or entity exercising rights under this License who has not previously violated the terms of this License with respect to the Work, or who has received express permission from the Licensor to exercise rights under this License despite a previous violation.
"Publicly Perform" means to perform public recitations of the Work and to communicate to the public those public recitations, by any means or process, including by wire or wireless means or public digital performances; to make available to the public Works in such a way that members of the public may access these Works from a place and at a place individually chosen by them; to perform the Work to the public by any means or process and the communication to the public of the performances of the Work, including by public digital performance; to broadcast and rebroadcast the Work by any means including signs, sounds or images.
"Reproduce" means to make copies of the Work by any means including without limitation by sound or visual recordings and the right of fixation and reproducing fixations of the Work, including storage of a protected performance or phonogram in digital form or other electronic medium.
2. Fair Dealing Rights. Nothing in this License is intended to reduce, limit, or restrict any uses free from copyright or rights arising from limitations or exceptions that are provided for in connection with the copyright protection under copyright law or other applicable laws.

3. License Grant. Subject to the terms and conditions of this License, Licensor hereby grants You a worldwide, royalty-free, non-exclusive, perpetual (for the duration of the applicable copyright) license to exercise the rights in the Work as stated below:

to Reproduce the Work, to incorporate the Work into one or more Collections, and to Reproduce the Work as incorporated in the Collections;
to create and Reproduce Adaptations provided that any such Adaptation, including any translation in any medium, takes reasonable steps to clearly label, demarcate or otherwise identify that changes were made to the original Work. For example, a translation could be marked "The original work was translated from English to Spanish," or a modification could indicate "The original work has been modified.";
to Distribute and Publicly Perform the Work including as incorporated in Collections; and,
to Distribute and Publicly Perform Adaptations.
For the avoidance of doubt:

Non-waivable Compulsory License Schemes. In those jurisdictions in which the right to collect royalties through any statutory or compulsory licensing scheme cannot be waived, the Licensor reserves the exclusive right to collect such royalties for any exercise by You of the rights granted under this License;
Waivable Compulsory License Schemes. In those jurisdictions in which the right to collect royalties through any statutory or compulsory licensing scheme can be waived, the Licensor waives the exclusive right to collect such royalties for any exercise by You of the rights granted under this License; and,
Voluntary License Schemes. The Licensor waives the right to collect royalties, whether individually or, in the event that the Licensor is a member of a collecting society that administers voluntary licensing schemes, via that society, from any exercise by You of the rights granted under this License.
The above rights may be exercised in all media and formats whether now known or hereafter devised. The above rights include the right to make such modifications as are technically necessary to exercise the rights in other media and formats. Subject to Section 8(f), all rights not expressly granted by Licensor are hereby reserved.

4. Restrictions. The license granted in Section 3 above is expressly made subject to and limited by the following restrictions:

You may Distribute or Publicly Perform the Work only under the terms of this License. You must include a copy of, or the Uniform Resource Identifier (URI) for, this License with every copy of the Work You Distribute or Publicly Perform. You may not offer or impose any terms on the Work that restrict the terms of this License or the ability of the recipient of the Work to exercise the rights granted to that recipient under the terms of the License. You may not sublicense the Work. You must keep intact all notices that refer to this License and to the disclaimer of warranties with every copy of the Work You Distribute or Publicly Perform. When You Distribute or Publicly Perform the Work, You may not impose any effective technological measures on the Work that restrict the ability of a recipient of the Work from You to exercise the rights granted to that recipient under the terms of the License. This Section 4(a) applies to the Work as incorporated in a Collection, but this does not require the Collection apart from the Work itself to be made subject to the terms of this License. If You create a Collection, upon notice from any Licensor You must, to the extent practicable, remove from the Collection any credit as required by Section 4(b), as requested. If You create an Adaptation, upon notice from any Licensor You must, to the extent practicable, remove from the Adaptation any credit as required by Section 4(b), as requested.
If You Distribute, or Publicly Perform the Work or any Adaptations or Collections, You must, unless a request has been made pursuant to Section 4(a), keep intact all copyright notices for the Work and provide, reasonable to the medium or means You are utilizing: (i) the name of the Original Author (or pseudonym, if applicable) if supplied, and/or if the Original Author and/or Licensor designate another party or parties (e.g., a sponsor institute, publishing entity, journal) for attribution ("Attribution Parties") in Licensor's copyright notice, terms of service or by other reasonable means, the name of such party or parties; (ii) the title of the Work if supplied; (iii) to the extent reasonably practicable, the URI, if any, that Licensor specifies to be associated with the Work, unless such URI does not refer to the copyright notice or licensing information for the Work; and (iv) , consistent with Section 3(b), in the case of an Adaptation, a credit identifying the use of the Work in the Adaptation (e.g., "French translation of the Work by Original Author," or "Screenplay based on original Work by Original Author"). The credit required by this Section 4 (b) may be implemented in any reasonable manner; provided, however, that in the case of a Adaptation or Collection, at a minimum such credit will appear, if a credit for all contributing authors of the Adaptation or Collection appears, then as part of these credits and in a manner at least as prominent as the credits for the other contributing authors. For the avoidance of doubt, You may only use the credit required by this Section for the purpose of attribution in the manner set out above and, by exercising Your rights under this License, You may not implicitly or explicitly assert or imply any connection with, sponsorship or endorsement by the Original Author, Licensor and/or Attribution Parties, as appropriate, of You or Your use of the Work, without the separate, express prior written permission of the Original Author, Licensor and/or Attribution Parties.
Except as otherwise agreed in writing by the Licensor or as may be otherwise permitted by applicable law, if You Reproduce, Distribute or Publicly Perform the Work either by itself or as part of any Adaptations or Collections, You must not distort, mutilate, modify or take other derogatory action in relation to the Work which would be prejudicial to the Original Author's honor or reputation. Licensor agrees that in those jurisdictions (e.g. Japan), in which any exercise of the right granted in Section 3(b) of this License (the right to make Adaptations) would be deemed to be a distortion, mutilation, modification or other derogatory action prejudicial to the Original Author's honor and reputation, the Licensor will waive or not assert, as appropriate, this Section, to the fullest extent permitted by the applicable national law, to enable You to reasonably exercise Your right under Section 3(b) of this License (right to make Adaptations) but not otherwise.
5. Representations, Warranties and Disclaimer

UNLESS OTHERWISE MUTUALLY AGREED TO BY THE PARTIES IN WRITING, LICENSOR OFFERS THE WORK AS-IS AND MAKES NO REPRESENTATIONS OR WARRANTIES OF ANY KIND CONCERNING THE WORK, EXPRESS, IMPLIED, STATUTORY OR OTHERWISE, INCLUDING, WITHOUT LIMITATION, WARRANTIES OF TITLE, MERCHANTIBILITY, FITNESS FOR A PARTICULAR PURPOSE, NONINFRINGEMENT, OR THE ABSENCE OF LATENT OR OTHER DEFECTS, ACCURACY, OR THE PRESENCE OF ABSENCE OF ERRORS, WHETHER OR NOT DISCOVERABLE. SOME JURISDICTIONS DO NOT ALLOW THE EXCLUSION OF IMPLIED WARRANTIES, SO SUCH EXCLUSION MAY NOT APPLY TO YOU.

6. Limitation on Liability. EXCEPT TO THE EXTENT REQUIRED BY APPLICABLE LAW, IN NO EVENT WILL LICENSOR BE LIABLE TO YOU ON ANY LEGAL THEORY FOR ANY SPECIAL, INCIDENTAL, CONSEQUENTIAL, PUNITIVE OR EXEMPLARY DAMAGES ARISING OUT OF THIS LICENSE OR THE USE OF THE WORK, EVEN IF LICENSOR HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.

7. Termination

This License and the rights granted hereunder will terminate automatically upon any breach by You of the terms of this License. Individuals or entities who have received Adaptations or Collections from You under this License, however, will not have their licenses terminated provided such individuals or entities remain in full compliance with those licenses. Sections 1, 2, 5, 6, 7, and 8 will survive any termination of this License.
Subject to the above terms and conditions, the license granted here is perpetual (for the duration of the applicable copyright in the Work). Notwithstanding the above, Licensor reserves the right to release the Work under different license terms or to stop distributing the Work at any time; provided, however that any such election will not serve to withdraw this License (or any other license that has been, or is required to be, granted under the terms of this License), and this License will continue in full force and effect unless terminated as stated above.
8. Miscellaneous

Each time You Distribute or Publicly Perform the Work or a Collection, the Licensor offers to the recipient a license to the Work on the same terms and conditions as the license granted to You under this License.
Each time You Distribute or Publicly Perform an Adaptation, Licensor offers to the recipient a license to the original Work on the same terms and conditions as the license granted to You under this License.
If any provision of this License is invalid or unenforceable under applicable law, it shall not affect the validity or enforceability of the remainder of the terms of this License, and without further action by the parties to this agreement, such provision shall be reformed to the minimum extent necessary to make such provision valid and enforceable.
No term or provision of this License shall be deemed waived and no breach consented to unless such waiver or consent shall be in writing and signed by the party to be charged with such waiver or consent.
This License constitutes the entire agreement between the parties with respect to the Work licensed here. There are no understandings, agreements or representations with respect to the Work not specified here. Licensor shall not be bound by any additional provisions that may appear in any communication from You. This License may not be modified without the mutual written agreement of the Licensor and You.
The rights granted under, and the subject matter referenced, in this License were drafted utilizing the terminology of the Berne Convention for the Protection of Literary and Artistic Works (as amended on September 28, 1979), the Rome Convention of 1961, the WIPO Copyright Treaty of 1996, the WIPO Performances and Phonograms Treaty of 1996 and the Universal Copyright Convention (as revised on July 24, 1971). These rights and subject matter take effect in the relevant jurisdiction in which the License terms are sought to be enforced according to the corresponding provisions of the implementation of those treaty provisions in the applicable national law. If the standard suite of rights granted under applicable copyright law includes additional rights not granted under this License, such additional rights are deemed to be included in the License; this License is not intended to restrict the license of any rights under applicable law.
Creative Commons Notice

Creative Commons is not a party to this License, and makes no warranty whatsoever in connection with the Work. Creative Commons will not be liable to You or any party on any legal theory for any damages whatsoever, including without limitation any general, special, incidental or consequential damages arising in connection to this license. Notwithstanding the foregoing two (2) sentences, if Creative Commons has expressly identified itself as the Licensor hereunder, it shall have all rights and obligations of Licensor.

Except for the limited purpose of indicating to the public that the Work is licensed under the CCPL, Creative Commons does not authorize the use by either party of the trademark "Creative Commons" or any related trademark or logo of Creative Commons without the prior written consent of Creative Commons. Any permitted use will be in compliance with Creative Commons' then-current trademark usage guidelines, as may be published on its website or otherwise made available upon request from time to time. For the avoidance of doubt, this trademark restriction does not form part of this License.

Creative Commons may be contacted at http://creativecommons.org/.
'''


from colour import rgbToHsb
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
        hue, saturation, brightness = rgbToHsb(red, green, blue)
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