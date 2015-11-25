import socket

class Server:
	host = None
	port = None
	buffer_size = None

	def __init__(self):
		self.host = 'localhost'
		self.port = 6283
		self.buffer_size = 1024
	
	def start_server(self):
		serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		serv_sock.bind((self.host,self.port))
		serv_sock.listen(1)

		conn, addr = serv_sock.accept()
		print("CONNECTION FROM:",addr)

		while True:
			data = conn.recv(self.buffer_size).decode()
			if not data: break
			print("Received: " + (data))
		
		conn.close()
		return
		


if __name__ == "__main__":
	a_server = Server()
	a_server.start_server()
	



