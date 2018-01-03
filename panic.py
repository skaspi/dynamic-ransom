#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 15:37:10 2017

@authors Rafael,Dmitriy
Ransomware Detection Project
Technion, Haifa, Israel

Script for sending appropriate info to Command & Control in
the case of ransomware attack:
            ** e-mail ID
            ** 'infected file' message
"""

import os
import time

import watch


def catastrophe():
    """
                Ransomware was detected --> send HTTP GET to C&C + stop machine
                + clean-up operations

    """
    print("Ransomware detected !!!")
    print("Sending signal to C&C  + clean-up operations")

    for worker in watch.threads:
        worker.stop()

    os.remove(os.environ['USERPROFILE'] + "\\Desktop\\script.py")
    print("Reboot in 3 seconds")
    time.sleep(3)


def main():
    catastrophe()


if __name__ == '__main__':
    main()
