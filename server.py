#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 22:45:16 2017

@authors Rafael,Dmitriy
Ransomware Detection Project
Technion, Haifa, Israel

Server that handle multiple C&C inbound connections with threads
Each request contains a list of suspicious links, which will be analyzed
by our Sand-Box mechanism.
A huge credit goes to Silver Moon and his post from the following link:
http://www.binarytides.com/python-socket-server-code-example/
We really appreciate it :))
"""
import socket
import sys
import threading


def client_thread(conn):
    """
    Function for handling connections. This will be used to create threads
    """
    while True:
        data = conn.recv(1024)
        reply = b'OK...' + data
        if not data:
            break
        conn.sendall(reply)
    conn.close()


def main():
    HOST = 'localhost'
    PORT = 8080

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Socket created')

    # Bind socket to local host and port
    try:
        s.bind((HOST, PORT))
    except socket.error as msg:
        print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
        sys.exit()

    print('Socket bind complete')

    s.listen(10)
    print('Socket now listening')

    while 1:
        conn, addr = s.accept()
        print('Connected with ' + addr[0] + ':' + str(addr[1]))
        t = threading.Thread(target=client_thread, args=(conn,))
        t.start()
    s.close()


if __name__ == '__main__':
    main()
