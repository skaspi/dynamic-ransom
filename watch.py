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
In our case we monitor C drive.

NOTE: The signal-handlers are playing important role:
      before the program terminates we need to traverse through all the randomly-generated files
      and clean them up.
"""
import atexit
import os
import shutil
import signal
import subprocess
import sys
import threading
import time


@atexit.register
def clean_up():
    """
        The actual treads stopping + files clean-up
    """

    for worker in threads:
        worker.stop()

    try:
        os.remove(os.environ['USERPROFILE'] + "\\Desktop\\script.py")

    except FileNotFoundError:
        pass

    sys.exit(0)


def exit_handler(signal, frame):
    """
        General shutdown signal handler
    """
    sys.stdout.write('\nStopping threads...clean-up files... ')
    sys.stdout.flush()
    clean_up()
    time.sleep(1)
    sys.stdout.write('done\n')
    sys.stdout.flush()


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
        else:
            aux_supervisor()

    def stop(self):
        self.kill_received = True


def aux_supervisor():
    """
         Watch after script.py  from ransom modification
    """
    shell = "C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe"
    arguments = "watchmedo shell-command --patterns='*.py' --recursive --command='python C:\\WINDOWS\\system32\\panic\\panic.py' "
    location = os.environ['USERPROFILE'] + "\\Desktop\\"
    subprocess.call([shell, arguments + location])


def supervisor():
    """
            Watch after honeypot files modification
    """
    shell = "C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe"
    arguments = "watchmedo shell-command --patterns='*.txt;*.pdf;*.xlsx' --recursive  --command='python "
    location = os.environ['USERPROFILE'] + "\\Desktop\\" + "script.py"
    subprocess.call([shell, arguments + location + " ${watch_src_path}' C:\\"])


def main():
    print("Watch-dog is getting started ...")

    global threads
    threads = []

    signal.signal(signal.SIGINT, exit_handler)
    signal.signal(signal.SIGTERM, exit_handler)
    signal.signal(signal.SIGBREAK, exit_handler)
    signal.signal(signal.SIGABRT, exit_handler)

    shutil.copy("script.py", os.environ['USERPROFILE'] + "\\Desktop\\")


    # Create new watch-dogs
    thread1 = thread(1, "watch-dog#1")
    thread2 = thread(2, "watch-dog#2")

    # Add threads to global list
    threads.append(thread1)
    threads.append(thread2)

    # Start new watch-dogs
    thread1.start()
    thread2.start()


if __name__ == '__main__':
    main()
