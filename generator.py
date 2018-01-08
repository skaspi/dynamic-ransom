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

import xlsxwriter

dictionary = ["work", "book", "network", "random", "honey", "file", "list", "subscription", "computer",                                                                                            "important", "spot",
              "system", "log", "area", "shape", "song", "generator", "crawler", "infection", "data"
              "auditor", "screen", "monitor", "desk", "table", "keys", "security", "random", "tube",
              "box", "picture", "language", "framework", "cable", "disc", "grades", "account", "salaries"]


def randomxls(path):
    """
       Generate .xls files in 'path' directory
    """
    num_of_files = 8

    words = []
    counter = 0

    with open('dictionary.txt', 'r') as f:
        for line in f:
            for word in line.split():
                words.append(word)
    f.close()

    for i in range(num_of_files):
        name = path + dictionary[counter] + ".xlsx"
        counter += 1
        name1 = path + dictionary[counter] + ".txt"
        counter += 1
        fh = open(name1, "w+")

        workbook = xlsxwriter.Workbook(name)
        worksheet = workbook.add_worksheet()

        numrows = 20

        for j in range(numrows):
            coord = 'A' + str(i)
            rnd = randint(0, len(words) - 1)
            textinrow = words[rnd]
            rnd = randint(0, len(words) - 1)
            textinrow_1 = words[rnd]
            fh.write(textinrow + " " + textinrow_1 + "\n")
            worksheet.write(coord, textinrow + " " + textinrow_1)

        workbook.close()
        fh.close()


def main():
    path = os.environ['USERPROFILE'] + "\\Desktop\\honey\\"

    if not os.path.exists(path):
        os.makedirs(path)

    randomxls(path)


if __name__ == '__main__':
    main()
