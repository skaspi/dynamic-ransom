import json
import socket

HOST = 'localhost'    # The remote host
PORT = 8080             # The same port as used by the server
links = ["ma", "ze", "da"]
out = json.dumps(links)
sent = out.encode('ASCII')
print(type(out))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(sent)
    data = s.recv(1024)
print('Received', repr(data))
