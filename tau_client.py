"""

Copyright (C) 2015 RJ Russell
Created with the collaborative assistance of::
Jacob Martin:
Rachael Johnson:
Andrew Wood:

References: Daniel Zappala..BYU Python Tutorial.http://ilab.cs.byu.edu/python/
            Python Docs:........................https://www.python.org/
"""

import socket
import rc4
PORT = 6253
BUFFERSIZE = 1024
class TauClient:
    def __init__(self, host, message, key='asdfg'):
        self.host = host
        self.message = message
        self.key = key

    def connect_client(self):
        print "Creating socket..."
        client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print "Connecting to host and port..."
        client_sock.connect((self.host, PORT))
        print "Connected..."
        print "Sending message..."
        self.send_message(client_sock)


    def send_message(self, client_sock):
        encrypt_mess = rc4.encrypt(self.message, self.key)
        client_sock.send(encrypt_mess)
        self.close_client(client_sock, encrypt_mess)

    def close_client(self, client_sock, encrypt_mess):
        client_sock.close()
        print "Received: ", encrypt_mess

if __name__ == '__main__':

    mess = raw_input("Enter Message: ")

    client = TauClient('localhost', mess)
    client.connect_client()



    #f = open("testfiles/test.cs1", "w")
	#message = raw_input("Enter your message: ")


	#z = encrypt(message, key2)
	#f.write(z)
	#f.close()

	#l = open("testfiles/test.cs1", "r")
	#message = l.read()
	#m = decrypt(message, key2)
	#print "Message: ", m, "\n"
	#l.close()





