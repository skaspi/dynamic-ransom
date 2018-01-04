#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 04 18:52:16 2017

@authors Rafael,Dmitriy
Ransomware Detection Project
Technion, Haifa, Israel

Script for cleaning the honeypot files
"""

import os


def remove_dir(directory):
    """
        Remove files within given directory
    """
    for dirName, dirlist, fileList in os.walk(directory):
        for fname in fileList:
            os.remove(directory + fname)


def main():
    path = os.environ['USERPROFILE'] + "\\Ransom\\"
    path_1 = os.environ['USERPROFILE'] + "\\Documents\\Love\\"
    path_2 = "C:\\We\\"

    remove_dir(path)
    remove_dir(path_1)
    remove_dir(path_2)


if __name__ == '__main__':
    main()
