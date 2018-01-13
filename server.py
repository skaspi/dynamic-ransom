#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 21:12:16 2017

@authors Rafael,Dmitriy
Ransomware Detection Project
Technion, Haifa, Israel


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
                print(data)
                conn.sendall(data)


if __name__ == '__main__':
    main()
