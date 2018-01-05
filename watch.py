#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 21:12:16 2017

@authors Rafael,Dmitriy
Ransomware Detection Project
Technion, Haifa, Israel

Script for watch-dog audition.The watch dog screens all the
changes(deleting,modifying etc.) made to files with specified extensions.
Each watch-dog screens its own directory.
"""
import atexit
import os
import shutil
import signal
import subprocess
import sys
import threading
import time

exited = 0

global threads
threads = []


def clean_up():
    """
        The actual treads stopping + files clean-up
    """
    global exited
    global threads

    if exited == 1:
        return

    sys.stdout.write('\nStopping threads...clean-up files... ')
    sys.stdout.flush()

    for worker in threads:
        worker.stop()

    cleaner()

    sys.stdout.write('done\n')
    sys.stdout.flush()
    exited = 1
    time.sleep(1)


def exit_handler(signal, frame):
    """
        General shutdown signal handler
    """
    clean_up()


class thread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.kill_received = False
        self.threadID = threadID
        self.name = name

    def run(self):
        print("Started: " + self.name)

        if self.threadID == 1:
            supervisor()

    def stop(self):
        self.kill_received = True


def cleaner():
    """
        Call the dedicated cleaner.py script
    """
    subprocess.Popen(["python", "cleaner.py"], shell=True, stdout=subprocess.PIPE).communicate()[0]


def crawler():
    """
        Extract the names of honeypots with dedicated crawler script
    """
    subprocess.Popen(["python", "crawler.py"], shell=True, stdout=subprocess.PIPE).communicate()[0]


def generate():
    """
        Call the dedicated generator.py script
    """
    subprocess.Popen(["python", "generator.py"], shell=True, stdout=subprocess.PIPE).communicate()[0]


def distribute():
    """
        Distribute honeypots to specified folders
    """

    path = os.environ['USERPROFILE'] + "\\Ransom\\"
    path_1 = os.environ['USERPROFILE'] + "\\Documents\\Love\\"
    path_2 = "C:\\We\\"

    if not os.path.exists(path):
        os.makedirs(path)

    if not os.path.exists(path_1):
        os.makedirs(path_1)

    if not os.path.exists(path_2):
        os.makedirs(path_2)

    counter = 0
    indicator = 0

    rootdir = os.environ['USERPROFILE'] + "\\Desktop\\honey\\"

    for dirName, dirlist, fileList in os.walk(rootdir):
        for fname in fileList:
            if indicator == 0:
                shutil.move(rootdir + fname, path + fname)
            elif indicator == 1:
                shutil.move(rootdir + fname, path_1 + fname)
            else:
                shutil.move(rootdir + fname, path_2 + fname)

            counter += 1

            if counter % 40 == 0:
                indicator += 1


def supervisor():
    """
        Watch after honeypot files modification
    """
    shell = "C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe"
    arguments = "watchmedo shell-command --patterns='*.txt;*.xlsx' --recursive  --command='python "
    location = "auditor.py"
    subprocess.call([shell, arguments + location + " ${watch_src_path}' C:\\"])


def main():
    print("Watch-dog is getting started ...")

    global threads

    atexit.register(clean_up)
    signals = [signal.SIGINT, signal.SIGTERM, signal.SIGBREAK, signal.SIGABRT]

    for sig in signals:
        signal.signal(sig, exit_handler)

    # Create new watch-dogs
    thread1 = thread(1, "watch-dog#1")

    # Add threads to global list
    threads.append(thread1)

    print("Generating honeypot files ...")
    generate()

    print("Distributing honeypots ...")
    crawler()
    distribute()

    # Start new watch-dogs
    for worker in threads:
        worker.start()


if __name__ == '__main__':
    main()
