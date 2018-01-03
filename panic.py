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
import sys
import time


def catastrophe():
    """
            Ransomware was detected --> send HTTP GET to C&C + clean-up
            + reboot
    """
    print("Ransomware detected !!!")
    print("Sending signal to C&C ...")

    print("Reboot in 3 seconds")
    time.sleep(3)
    sys.exit(0)


def main():
    catastrophe()


if __name__ == '__main__':
    main()
