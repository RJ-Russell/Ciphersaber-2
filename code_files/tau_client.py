"""

Copyright (C) 2015 RJ Russell
Created with the collaborative assistance of::
Jacob Martin, Rachael Johnson, Andrew Wood:

References: Daniel Zappala..BYU Python Tutorial.http://ilab.cs.byu.edu/python/
            Python Docs:........................https://www.python.org/


 tau_client.py

 This file is responsible for taking in a message, connecting to the recipient's
 address and port number, sending the message to be encrypted, and then sending
 the message to the intended recipient. The user interface for this file is
 tau_interface.py.
"""


import socket
import rc4

PORT = 6283
BUFFERSIZE = 1024


class TauClient:
    def __init__(self, key='password'):
        """ Initializes all values for the client sockets and for the message encryption """
        self.host = None
        self.message = None
        self.key = key
        self.client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_client(self, host, message):
        """
        :param host: Passed in from the tau_interface. Initializes recipients address.
        :param message: Passed in from the tau_interface. Message to be sent to recipient
        :return: Returns -1 if message cannot be sent due to socket timeout.
        """
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
        """ Catches the returned encrypted message and sends it to the recipient then closes socket """
        encrypt_mess = rc4.encrypt(self.message, self.key)
        print "Sending message..."
        self.client_sock.send(encrypt_mess)
        print "Sent encrypted message!"
        self.close_client()

    def close_client(self):
        """  Correctly closes the sockets """
        try:
            self.client_sock.shutdown(socket.SHUT_RDWR)
            self.client_sock.close()
            print "Sockets Closed"
        except:
            print "Socket Close Error"

