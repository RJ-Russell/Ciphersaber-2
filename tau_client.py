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
    def __init__(self, host, key='asdfg'):
        self.host = host
        self.key = key

    def connect_client(self):
        while True:
            print "Creating socket..."
            client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print "Connecting to host and port..."
            client_sock.connect((self.host, PORT))
            print "Connected..."
            print "Sending message..."
            self.send_message(client_sock)

    def send_message(self, client_sock):

        message = raw_input("Enter Message: ")
        if message == "exit":
            self.close_client(client_sock)

        encrypt_mess = rc4.encrypt(message, self.key)
        client_sock.send(encrypt_mess)

        print "Received: ", encrypt_mess

    def close_client(self, client_sock):
        client_sock.close()


if __name__ == '__main__':
    client = TauClient('localhost')
    client.connect_client()



