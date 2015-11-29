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
import socket
import rc4

HOST = ''
PORT = 6283
BUFFERSIZE = 1024
BACKLOG = 5


class TauServer:
    def connect_server(self):
        serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serv_socket.bind((HOST, PORT))
        serv_socket.listen(BACKLOG)

        while 1:
            client, address = serv_socket.accept()
            message = client.recv(BUFFERSIZE)
            if message:
                dec_mess = rc4.decrypt(message, key='password')
                print "Received from ", client, ": ", dec_mess
                client.send(dec_mess)

                # client.close()




if __name__ == '__main__':
    server = TauServer()
    server.connect_server()
