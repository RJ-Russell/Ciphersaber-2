import socket


HOST = '71.239.196.3'
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
