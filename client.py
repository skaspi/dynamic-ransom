import json
import socket

HOST = '1ocalhost'
PORT = 8080
links = ['https://download.sysinternals.com/files/Sysmon.zip',
         'https://download.sysinternals.com/files/ClockRes.zip',
         'https://download.sysinternals.com/files/AutoLogon.zip',
         'https://download.sysinternals.com/files/PSTools.zip']
out = json.dumps(links)
sent = out.encode('ASCII')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(sent)
    data = s.recv(1024)
print('Received', repr(data))
