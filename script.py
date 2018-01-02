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
import sys
import time
import subprocess


def panic():
    shell = "C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe"
    arguments = "C:\\WINDOWS\\system32\\panic\\panic.exe"
    subprocess.call([shell, arguments])


def aux_check(ans, value, mode):
    if mode == "r":
        if not ans and value == 0:
            return True

    else:
        if not ans and value == 1:
            return True

    return False


def open_file(param, mode):
    value = -1

    try:
        fh = open(os.environ['USERPROFILE'] + "\\Desktop\\counter.bak", mode)

    except IOError:
        return False, -1

    try:
        if mode == "r":
            data = fh.readline()
            value = int(data)

    except ValueError:
        print("Failed to convert str to int")
        fh.close()
        return False, 0

    try:
        if mode == "w":
            fh.write(param)

    except IOError as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))
        fh.close()
        return False, 1

    fh.close()
    return True, value


def main():
    print("Detected : ", sys.argv[1])

    error_num = 0
    ans, value = open_file(-1, "r")

    if (not ans and value == -1) or value >= 40:
        panic()
        return

    while error_num < 3 and aux_check(ans, value, "r"):
        time.sleep(1)
        ans, value = open_file(-1, "r")
        error_num += 1

    if error_num < 3:
        value += 1
        error_num = 0

    else:
        panic()
        return

    ans, value = open_file(str(value), "w")

    while error_num < 3 and aux_check(ans, value, "w"):
        time.sleep(1)
        ans, value = open_file(str(value), "w")
        error_num += 1

    if error_num == 3:
        print("Corrupted file !!!")


if __name__ == '__main__':
    main()
