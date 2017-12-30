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
In our case we monitor C:\\ drive.

"""
import os
import shutil
import subprocess
import threading


class myThread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        print("Started: " + self.name)

        if self.threadID == 1:
            supervisor()
        else:
            aux_supervisor()


def aux_supervisor():
    shell = "C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe"
    arguments = "watchmedo shell-command --patterns='*.py' --recursive --command='echo hui' "
    location = os.environ['USERPROFILE'] + "\\Desktop\\"
    subprocess.call([shell, arguments + location])


def supervisor():
    shell = "C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe"
    arguments = "watchmedo shell-command --patterns='*.txt;*.pdf;*.xlsx' --recursive  --command='python "
    location = os.environ['USERPROFILE'] + "\\Desktop\\" + "script.py"
    subprocess.call([shell, arguments + location + " ${watch_src_path}' C:\\"])


def main():
    print("Watch-dog is getting started ...")

    fh = open(os.environ['USERPROFILE'] + "\\Desktop\\counter.bak", "w+")
    shutil.copy("script.py", os.environ['USERPROFILE'] + "\\Desktop\\")
    fh.write("0")
    fh.close()

    # Create new watch-dogs
    thread1 = myThread(1, "watch-dog#1")
    thread2 = myThread(2, "watch-dog#1")

    # Start new watch-dogs
    thread1.start()
    thread2.start()


if __name__ == '__main__':
    main()
