import socket
import json

class server:
#	connections = json.load(open(tau_table.json))
#	send_to = None
#	received_from = None


	port = 6283
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind(('0.0.0.0',port))
	sock.listen(1)

	print("Listening on port:",port)

	while(1):
		conn, sock_addr = sock.accept()
		print("Accepted connection from: ", sock_addr)
		while 1:
			command = input('shell> ')
			conn.send(command)
			data = conn.recv(6283)
			if not data:
				break;
			print(data)

#	socket.gethostbyname(sent_to) # dns ip resolution
	
#	s = socket.socket(socket.AF_INET.SOCK_STREAM)
#	s.bind((HOST,PORT))
#	s.listen(1)

#	conn, addr = s.accept()

#	print ("Connected by: ", addr)

#	while 1:
 #		data = conn.recv(1024)
  #		if not data: break
   #	conn.sendall(data)

	#conn.close()

#	TCP_IP = '127.0.0.1'
#	7 TCP_PORT = 5005
 #	8 BUFFER_SIZE = 1024
 #	9 MESSAGE = "Hello, World!"
 # 10 
 # 11 s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 # 12 s.connect((TCP_IP, TCP_PORT))
 # 13 s.send(MESSAGE)
 # 14 data = s.recv(BUFFER_SIZE)
 # 15 s.close()
 # 16 
 # 17 print "received data:", data
