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

import os
import re
import subprocess
import sys
import time

import panic


def panic():
    """
            Ransomware detected --> invoke the PANIC routine
    """
    subprocess.Popen(["python", "panic.py"], shell=True, stdout=subprocess.PIPE).communicate()[0]


def main():
    flag = 0
    filename = os.path.basename(sys.argv[1])

    try:
        file = open("names.txt", "r")
        text = file.read()
        file.close()
        result = re.findall("\\b" + filename + "\\b", text)

        if result.__len__() != 0:
            flag = 1

    except IOError:
        pass

    print("Detected : {0} , is honeypot file ------> {1}".format(sys.argv[1], flag == 1))

    if flag == 1:
        time.sleep(1)
        panic()


if __name__ == '__main__':
    main()
