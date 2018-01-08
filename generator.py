#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 1 12:50:16 2018

@authors Rafael,Dmitriy
Ransomware Detection Project
Technion, Haifa, Israel

Auxiliary script for generating honeypot files with random names and content.
Currently, we generating *.txt,*.xlsx files.
"""

import os.path
from random import randint
from shutil import copyfile, SameFileError

import xlsxwriter

dictionary = ["work", "book", "network", "random", "honey", "file", "list", "subscription", "computer"
                                                                                            "important", "spot",
              "system", "log", "area", "shape", "song", "generator", "crawler",
              "auditor", "screen", "monitor", "desk", "table", "keys", "security", "random", "tube",
              "box", "picture", "language", "framework", "cable", "disc", "grades", "account", "salaries"]


def randomxls(path):
    """
       Generate .xls files in 'path' directory
    """
    numxls = 5

    for i in range(5):

        rnd = randint(0, len(dictionary) - 1)
        name = path + dictionary[rnd] + ".xlsx"
        rnd = randint(0, len(dictionary) - 1)
        name1 = path + dictionary[rnd] + ".txt"
        fh = open(name1, "w+")

        workbook = xlsxwriter.Workbook(name)
        worksheet = workbook.add_worksheet()

        numrows = 20
        words = []

        with open('dictionary.txt', 'r') as f:
            for line in f:
                for word in line.split():
                    words.append(word)
        f.close()

        for i in range(numrows):
            coord = 'A' + str(i)
            rnd = randint(0, len(words) - 1)
            textinrow = words[rnd]
            rnd = randint(0, len(words) - 1)
            textinrow_1 = words[rnd]
            fh.write(textinrow + " " + textinrow_1 + "\n")
            worksheet.write(coord, textinrow + " " + textinrow_1)

        workbook.close()
        fh.close()

        for i in range(numxls):
            if i != 0 and i % 4 == 0:
                rnd = randint(0, len(dictionary) - 1)
                duplicate = path + dictionary[rnd] + ".xlsx"
                rnd = randint(0, len(dictionary) - 1)
                duplicate1 = path + dictionary[rnd] + ".txt"

                try:
                    copyfile(name, duplicate)
                except SameFileError:
                    pass
                try:
                    copyfile(name1, duplicate1)
                except SameFileError:
                    pass


def main():
    path = os.environ['USERPROFILE'] + "\\Desktop\\honey\\"

    if not os.path.exists(path):
        os.makedirs(path)

    randomxls(path)


if __name__ == '__main__':
    main()
