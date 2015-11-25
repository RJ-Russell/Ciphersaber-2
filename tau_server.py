import socket

class Server:
	host = None
	port = None
	buffer_size = None

	def __init__(self, ):
		

	def start_server():
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.bind((HOST,PORT))
		s.listen(1)

		conn, addr = s.accept()
		print("CONNECTION FROM:",addr)

		while True:
			data = conn.recv(BUFFER_SIZE).decode()
			if not data: break
			print("Received: " + (data))
			response = input("Reply: ")
			if response == "exit":
				break
			conn.sendall(response.encode())
		conn.close()


if __name__ == "__main__":
	a_server = Server()


