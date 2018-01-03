#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 2 12:13:16 2018

@authors Rafael,Dmitriy
Ransomware Detection Project
Technion, Haifa, Israel

Auxiliary script for crawling through honeypot files and
saving their names.
"""

import os


def main():
    names = []
    rootdir = "."

    for dirName, subdirList, fileList in os.walk(rootdir):
        for fname in fileList:
            filename, file_extension = os.path.splitext(fname)
            if file_extension == ".txt" or file_extension == ".pdf" or file_extension == ".xlsx":
                names.append(filename + file_extension)

    file = open("names.txt", "w+")
    for name in names:
        file.write(name + "\n")
    file.close()


if __name__ == '__main__':
    main()
