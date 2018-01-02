#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 15:09:10 2017

@authors Rafael,Dmitriy
Ransomware Detection Project
Technion, Haifa, Israel

Auxiliary script for counting the number of times a files with given extensions were modified/deleted.
Ransomware Attack will be detected if an arbitrary number of honey-pots files are changed.
The number of modifications is stored in dedicated .bak file.
"""

import re
import subprocess
import sys
import time


def panic():
    shell = "C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe"
    arguments = "C:\\WINDOWS\\system32\\panic\\panic.exe"
    subprocess.call([shell, arguments])


def main():
    flag = 0

    filename = sys.argv[1].rsplit('\\', 1)[1]

    try:
        file = open("names.txt", "r")
        text = file.read()
        result = re.findall("\\b" + filename + "\\b", text)

        if result.__len__() != 0:
            flag = 1

        file.close()

    except IOError:
        pass

    print("Detected : {0} , is honeypot file ------> {1}" .format(sys.argv[1], flag == 1))

    if flag == 1:
        time.sleep(3)
        panic()


if __name__ == '__main__':
    main()
