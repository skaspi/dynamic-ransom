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


def main():
    HOST = 'localhost'  # Symbolic name meaning all available interfaces
    PORT = 8080  # Arbitrary non-privileged port

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Socket created')

    # Bind socket to local host and port
    try:
        s.bind((HOST, PORT))
    except socket.error as msg:
        print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
        sys.exit()

    print('Socket bind complete')

    # Start listening on socket
    s.listen(10)
    print('Socket now listening')

    # Function for handling connections. This will be used to create threads
    def clientthread(conn):
        # infinite loop so that function do not terminate and thread do not end.
        while True:

            # Receiving from client
            data = conn.recv(1024)
            reply = b'OK...' + data
            if not data:
                break

            conn.sendall(reply)

        # came out of loop
        conn.close()

    # now keep talking with the client
    while 1:
        # wait to accept a connection - blocking call
        conn, addr = s.accept()
        print('Connected with ' + addr[0] + ':' + str(addr[1]))

        # start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
        t = threading.Thread(target=clientthread, args=(conn,))
        t.start()

    s.close()


if __name__ == '__main__':
    main()
