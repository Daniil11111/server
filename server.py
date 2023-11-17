import socket
import threading
sock = socket.socket()
print(socket.getservbyname(socket.gethostname()))
sock.bind((socket.getservbyname(socket.gethostname()),17666))
sock.listen()

while True:
    client, addr = sock.accept()
    print(client.recv(2048))
    cliend.send(b'1')

sock.close()