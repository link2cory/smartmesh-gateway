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

#============================ defines =========================================
DEFAULT_PORT = '/dev/ttyO1'

#============================ main ============================================

def main():
    global connector
    connector  = IpMgrConnectorSerial()
    serialPort = DEFAULT_PORT

    # logging.config.fileConfig('logging.conf')
    try:
        connector.connect({
                            'port': serialPort,
                         })
    except ConnectionError as err:
        print err

    subscriber = IpMgrSubscribe(connector)
    subscriber.start()
    subscriber.subscribe(
        notifTypes = [subscriber.NOTIFDATA,],
        fun = NotificationRouter.routeNotification,
        isRlbl = False,
    )

    signal.pause()

# def mainTearDown():
#     try:
#         connector.disconnect()
#     except (ConnectionError,CommandTimeoutError) as err:
#         print err
#     print 'done.'
#     raw_input('\nScript ended. Press Enter to exit.')

if __name__ == "__main__":
    main()


