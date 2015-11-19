import socket


HOST = '127.0.0.1'
PORT = 6283
BUFFER_SIZE = 1024

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
