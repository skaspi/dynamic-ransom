#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 22:45:16 2017

@authors Rafael,Dmitriy
Ransomware Detection Project
Technion, Haifa, Israel

It is our server that listening to the C&C inbound requests.
Each request contains a list of suspicious links, which will be analyzed
by our Sand-Box mechanism.
"""
import socket


def main():
    HOST = 'localhost'  # Symbolic name meaning all available interfaces
    PORT = 8080  # Arbitrary non-privileged port
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data: break
                print(repr(data))
                conn.sendall(data)


if __name__ == '__main__':
    main()
