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
"""
import json
import multiprocessing
import os
import re
import shutil
import socket
import subprocess
import sys
import threading
import time
import zipfile
from urllib.request import urlopen

import requests

connection = 0


class thread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        url_download(self.name)


def watch_dog_run(user, sender):
    shell = "C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe"
    watch_dog = "C:\\WINDOWS\\system32\\watch\\watch.exe " + user + " " + sender

    os.chdir("C:\\WINDOWS\\system32\\watch\\")

    subprocess.call([shell, watch_dog])


def launch(root, user, sender):
    """
     Launch the user's .exe files
    """
    shell = "C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe"

    p = multiprocessing.Process(target=watch_dog_run, args=(user, sender,))
    p.start()

    for root, dirs, files in os.walk(root, topdown=False):
        for name in files:
            argument = os.path.join(root, name)
            time.sleep(0.5)
            subprocess.call([shell, argument])


def remove_redundant(root):
    """
     Remove redundant files from current user directory
    """
    for dirName, dirlist, fileList in os.walk(root):
        for fname in fileList:
            filename, file_extension = os.path.splitext(fname)
            if file_extension != ".exe":
                os.remove(root + filename + file_extension)


def url_download(url):
    """
     Download single file from given url
    """
    if not os.path.exists(str(connection)):
        try:
            os.makedirs(str(connection))
        except FileExistsError:
            pass

    folder = str(connection)
    request = requests.get(url)
    cd = request.headers.get('content-disposition')
    if cd:
        filename = get_filename_from_cd(cd)
    else:
        filename = url.rsplit('/', 1)[1]

    dir = filename.rsplit('.', 1)[0]
    os.chdir(folder)

    try:
        os.makedirs(dir)
    except FileExistsError:
        pass

    os.chdir("..")

    path = os.getcwd() + "\\" + folder + "\\" + dir + "\\"

    with urlopen(url) as response, open(path + filename, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)
        out_file.close()

    zip_ref = zipfile.ZipFile(path + filename, 'r')
    encrypt = 0

    try:
        zip_ref.testzip()
    except RuntimeError as e:
        if 'encrypted' in str(e):
            zip_ref.extractall(path, pwd=b'infected')
            encrypt = 1

    if encrypt == 0:
        zip_ref.extractall(path)

    zip_ref.close()
    os.remove(path + filename)
    remove_redundant(path)


def get_filename_from_cd(cd):
    """
     Auxiliary function for extracting filename from content-disposition
    """
    if not cd:
        return None
    fname = re.findall('filename=(.+)', cd)
    if len(fname) == 0:
        return None
    return fname[0]


def handle_links(raw_data, user, sender):
    """
     Routine for handling the received downloadable links
    """
    threads = []

    for i in range(len(raw_data)):
        thread_ = thread(i, raw_data[i])
        threads.append(thread_)

    for worker in threads:
        worker.start()

    for worker in threads:
        worker.join()

    src = os.getcwd() + "\\" + str(connection) + "\\"
    dst = os.environ['USERPROFILE'] + "\\Desktop\\" + str(connection)

    shutil.move(src, dst)
    launch(dst, user, sender)


def client_thread(conn):
    """
    Function for handling connections. This will be used to create threads
    """
    while True:
        data = conn.recv(2048)

        if not data:
            break
        my_json = data.decode('ASCII')
        data = json.loads(my_json)
        if type(data) == list:
            data = ''.join(data)
        else:
            data = json.loads(data)

        body_links = (re.findall("(?P<url>https?://[^\s]+)", data))

        user = "skaspi33@gmail.com"
        sender = "bad_guy@gmail.com"
        handle_links(body_links, user, sender)
        reply = b'OK...'
        conn.sendall(reply)

    conn.close()


def main():
    HOST = 'localhost'
    PORT = 8080
    global connection
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
        connection += 1
        t.start()
    s.close()


if __name__ == '__main__':
    main()
