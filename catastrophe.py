#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 15:37:10 2017

@authors Rafael,Dmitriy
Ransomware Detection Project
Technion, Haifa, Israel


"""

import time


def catastrophe():
    print("Ransomware detected !!!")
    print("Sending signal to C&C  ...")
    print("Reboot in 3 seconds")

    # open socket + reboot
    time.sleep(3)


def main():
    catastrophe()


if __name__ == '__main__':
    main()
