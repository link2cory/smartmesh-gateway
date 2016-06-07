#!/usr/bin/python

#============================ imports =========================================

import sys
import os
import time
import signal
import logging.config

from server import server
#============================ main ============================================

def main():
    Server.start_server()

if __name__ == "__main__":
    main()


