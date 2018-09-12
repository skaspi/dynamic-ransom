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


def crawl(directory):
    """
     Record the names of files that exist in current dir
    """
    names = []
    extensions = [".jpg", ".mp3", ".txt", ".xlsx", ".mp4"]

    for dirName, dirlist, fileList in os.walk(directory):
        for fname in fileList:
            filename, file_extension = os.path.splitext(fname)
            if file_extension in extensions:
                names.append(filename + file_extension)

    file = open("names.txt", "a+")
    for name in names:
        file.write(name + "\n")
    file.close()


def main():
    crawl(os.environ['USERPROFILE'] + "\\Desktop\\honey\\")
    crawl(os.environ['USERPROFILE'] + "\\Pictures\\")
    crawl(os.environ['USERPROFILE'] + "\\Music\\")
    crawl(os.environ['USERPROFILE'] + "\\Videos\\")


if __name__ == '__main__':
    main()
