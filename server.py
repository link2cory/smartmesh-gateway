#!/usr/bin/python

#============================ imports =========================================

import sys
import os
import time
import signal
import logging.config

from SmartMeshSDK.IpMgrConnectorSerial.IpMgrConnectorSerial import IpMgrConnectorSerial
from SmartMeshSDK.IpMgrConnectorMux.IpMgrSubscribe          import IpMgrSubscribe

from NotificationRouter import NotificationRouter

#========================== constants =========================================
DEFAULT_PORT = '/dev/ttyO1'

class server(object):

    notification_types = {
        'notifData': self._route_data,
    }
    @staticmethod
    def start_server():
        server()
        signal.pause()


    def __init__(self):
        self.connector = IpMgrConnectorSerial()
        serial_port = DEFAULT_PORT
        try:
            self.connector.connect({
                                'port': serial_port,
                             })
        except ConnectionError as err:
            print err


        self.subscriber = IpMgrSubscribe(connector)
        self.subscriber.start()
        self.subscriber.subscribe(
            notifTypes = [subscriber.NOTIFDATA,],
            fun = self.route_notification,
            isRlbl = False,
        )


    def route_notification(notifName, notifParams):
        self.notification_types[notifName](notifParams)

    def _route_data(data):
        packet = {
            'timestamp':     float(data.utcSecs)+float(data.utcUsecs/1000000.0),
            'mac':           tuple(data.macAddress),
            'srcPort':       data.srcPort,
            'destPort':      data.dstPort,
            'payload':       [b for b in data.data],
        }

        # format the packet's payload
        packet['payload'] = self._format_payload(packet['payload'])

        # print payload
        self._process_data(packet)

    def _format_payload(payload):
        # currently we are only sending moisture data
        return {
            'moisture': self._convert_little_endian_to_dec(payload[0:2]),
        }

    def _convert_little_endian_to_dec(little_endian):
        return int(
            ''.join(bin(b)[2:].zfill(8) for b in reversed(little_endian)),
            2
        )

    def _process_data(packet):
        print packet