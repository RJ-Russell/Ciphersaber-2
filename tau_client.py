# This will be the client portion of the TauNet messaging system
import json
import socket

host = '127.0.0.1'
port = 6283

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
print("Connected to " + (host) + "on Port: " + str(port))
initialMessage = input("Send: ")
s.sendall(initialMessage.encode())

while True:
    data = s.recv(1024).decode()
    print("Received: " + (data))
    response = input("Reply: ")
    if response == "exit":
        break
    s.sendall(response.encode())
s.close()




































#MSGLEN = 300



#hosts = chupa-cabra.ddns.net
#total_sent = 0
#while totalsent < MSGLEN:
#    sent = sock.sent(msg[total_sent])
#    if sent == 0:
#        raise RunTimeError("Socket Connection Broken")
#    total_sent = total_sent + sent




#msg = input("Enter the message: ")



# get dna resoltion
# client (receive message)



# possible send from a different high number port
# client (receiving)
# include tcp

# listen port 6238
# on receive: print message
#
#
# server (sends messages)
# include tcp
# open connection to client ip & client port
# send message
#
#
#
# client side (sending messages)
# server side (receiving messages)
# user interface
# rc4
#
# urandom on front of key
#
#
# if can run program and get cyphertext out , should be able to
# decrypt with the save IV and same key to get message back out
#
# watch for more than one 0 in array...only one character can encrypt to itself
