"""

Copyright (C) 2015 RJ Russell
Created with the collaborative assistance of::
Jacob Martin:
Rachael Johnson:
Andrew Wood:

References: Daniel Zappala..BYU Python Tutorial.http://ilab.cs.byu.edu/python/
            Python Docs:........................https://www.python.org/
"""
#
# tau_client.py

import socket
import rc4

PORT = 6283
BUFFERSIZE = 1024


class TauClient:
    def __init__(self, key='password'):
        self.host = None
        self.message = None
        self.key = key
        self.client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_client(self, host, message):

        self.host = host
        self.message = message
        print "Creating socket..."
        print "Connecting to host and port..."
        try:
            self.client_sock.settimeout(10)
            self.client_sock.connect((self.host, PORT))
            print "Connected..."
            self.send_message()
        except socket.error:
            print "Cannot connect at this time"
            self.client_sock.close()
            return -1

    def send_message(self):
        encrypt_mess = rc4.encrypt(self.message, self.key)
        print "Sending message..."
        self.client_sock.send(encrypt_mess)
        print "Sent encrypted message!"
        self.close_client()

    def close_client(self):
        try:
            self.client_sock.shutdown(socket.SHUT_RDWR)
            self.client_sock.close()
            print "Sockets Closed"
        except:
            print "Connection Closed"

        # if __name__ == '__main__':
        # client = TauClient('pi.arenjae.com')
        # client = TauClient('chupa-cabra.ddns.net')
        # client = TauClient('minion.mindtax.net','abcdf')
        # client = TauClient('megmurry.ddns.net')
        # client = TauClient('junkgrave.com')
        # client.connect_client()
