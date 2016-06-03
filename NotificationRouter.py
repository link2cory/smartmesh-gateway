import sys
import os
import time
import struct
import logging.config

class NotificationRouter(object):

    @staticmethod
    def routeNotification(notifName, notifParams):

        notification_types = {
            'notifData': NotificationRouter.routeData,
        }
        notification_types[notifName](notifParams)

    @staticmethod
    def routeData(notifParams):
        packet = {
            'timestamp':     float(notifParams.utcSecs)+float(notifParams.utcUsecs/1000000.0),
            'mac':           tuple(notifParams.macAddress),
            'srcPort':       notifParams.srcPort,
            'destPort':      notifParams.dstPort,
            'payload':       [b for b in notifParams.data],
        }

        # format the packet's payload
        payload = NotificationRouter._formatPayload(packet['payload'])
        print payload

        # send the payload to the server and await a response
        # NotificationRouter.

    @staticmethod
    def _formatPayload(payload):
        # currently we are only sending moisture data
        return {
            'moisture': NotificationRouter._convertLittleEndianToDec(payload[0:2]),
        }

    @staticmethod
    def _convertLittleEndianToDec(little_endian):
        # for b in reversed(payload):
        #     print bin(b)[2:]
        return int(
            ''.join(bin(b)[2:].zfill(8) for b in reversed(little_endian)),
            2
        )

