#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 04 18:52:16 2017

@authors Rafael,Dmitriy
Ransomware Detection Project
Technion, Haifa, Israel

Script for cleaning the paths from honeypot files
"""

import os


def clean_dir(directory, names):
    """
        Remove honeypot files from given directory
    """

    for dirName, dirlist, fileList in os.walk(directory):
        for fname in fileList:
            if fname in names:
                os.remove(directory + fname)


def main():
    """
            Collecting the paths and sending them for "clean-up"
    """
    paths = [os.environ['USERPROFILE'] + "\\Documents\\",
             os.environ['USERPROFILE'] + "\\Desktop\\"]

    f = open('names.txt', 'r')
    names = f.read().splitlines()
    f.close()

    for path in paths:
        clean_dir(path, names)

    os.remove(os.getcwd() + "\\names.txt")

    try:
        os.remove(os.getcwd() + "\\communicate.txt")
        os.remove(os.getcwd() + "\\data.txt")
    except FileNotFoundError:
        pass


if __name__ == '__main__':
    main()
