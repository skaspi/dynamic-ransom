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


def clean_dir(directory):
    """
        Remove honeypot files from given directory
    """
    for dirName, dirlist, fileList in os.walk(directory):
        for fname in fileList:
            os.remove(directory + fname)


def main():
    """
            Collecting the paths and sending them for "clean-up"
    """
    paths = ["C:\\", "C:\\Program Files\\", os.environ['USERPROFILE'] + "\\Pictures\\",
             os.environ['USERPROFILE'] + "\\Documents\\", os.environ['USERPROFILE'] + "\\Desktop\\"]

    for path in paths:
        clean_dir(path)



if __name__ == '__main__':
    main()
