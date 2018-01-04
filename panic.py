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
import time


def main():
    """
            Ransomware was detected --> send HTTP GET to C&C + clean-up
            + reboot
    """
    print("Ransomware detected !!!")
    print("Sending signal to C&C + cleaning the files...")

    # subprocess.Popen(["python", "cleaner.py"], shell=True, stdout=subprocess.PIPE).communicate()[0]

    print("Reboot in 3 seconds")
    time.sleep(1)


if __name__ == '__main__':
    main()
