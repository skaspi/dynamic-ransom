#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 15:09:10 2017

@authors Rafael,Dmitriy
Ransomware Detection Project
Technion, Haifa, Israel

Auxiliary script for monitoring the honeypot files.
Ransomware Attack will be detected if at least one of these files is modified.
"""

import os
import re
import signal
import sys


def panic():
    """
            Ransomware was detected --> send HTTP POST to C&C + kill VM instance
    """
    os.kill(os.getppid(), signal.CTRL_C_EVENT)


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

    if flag == 1:
        print("Detected honeypot modification : {0} ".format(sys.argv[1]))
        panic()


if __name__ == '__main__':
    main()
