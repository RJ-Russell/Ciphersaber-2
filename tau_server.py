"""

Copyright (C) 2015 RJ Russell
Created with the collaborative assistance of::
Jacob Martin:
Rachael Johnson:
Andrew Wood:

References: Daniel Zappala..BYU Python Tutorial.http://ilab.cs.byu.edu/python/
            Python Docs:........................https://www.python.org/
"""

# tau_server.py
import signal
import sys
import socket
import rc4

HOST = ''
PORT = 6283
BUFFERSIZE = 1024
BACKLOG = 5


class TauServer:
    def connect_server(self):
        serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        serv_socket.bind((HOST, PORT))
        serv_socket.listen(BACKLOG)

        while 1:
            try:
                print "\n\nLisening on port:", PORT
                print "(Press Control-C to Exit Server...)\n\n"
                client, address = serv_socket.accept()
            except KeyboardInterrupt:
                serv_socket.close()
                print "\nYou pressed Control-C..."
                print "\n\nDisconnected from Server.\n"
                exit(0)

            message = client.recv(BUFFERSIZE)
            if message:
                dec_mess = rc4.decrypt(message, key='password')
                print dec_mess
                client.send(dec_mess)






    # client.close()


if __name__ == '__main__':
    server = TauServer()
    server.connect_server()
