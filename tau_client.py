# This will be the client portion of the TauNet messaging system
import json
import socket
import threading 

# get address to send to
# enter message and encrypt it
# append header information
# send message to recipient 

class Client:
	host = None
	port = None
	buffer_size = None
	
	def __init__(self, host='localhost', port=6283, buffer_size=1024):
		self.host = host
		self.port = port
		self.buffer_size = buffer_size


	def start_client(self):
		while True:
			sock_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock_client.connect((self.host,self.port))
			print("Connected to " + (self.host) + " on Port: " + str(self.port))
			outgoing_message = raw_input("Send: ")
			sock_client.sendall(outgoing_message.encode())

			if outgoing_message == "exit":
				break
			#sock_client.sendall(outgoing_message.encode())
		sock_client.close()

if __name__ == "__main__":
	a_client = Client()
	a_client.start_client()
