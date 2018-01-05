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
import random
import string
from random import randint
from shutil import copyfile

import xlsxwriter


def randomxls(path):
    """
       Generate .xls files in 'path' directory
    """
    numxls = 5

    for i in range(5):

        name = path + ''.join(
            [random.choice(string.ascii_letters + string.digits) for n in range(randint(5, 15))]) + ".xlsx"
        name1 = path + ''.join(
            [random.choice(string.ascii_letters + string.digits) for n in range(randint(5, 15))]) + ".txt"
        fh = open(name1, "w+")

        workbook = xlsxwriter.Workbook(name)
        worksheet = workbook.add_worksheet()

        numrows = 5

        for i in range(numrows):
            coord = 'A' + str(i)

            textinrow = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(randint(5, 15))])
            fh.write(textinrow + "\n")
            worksheet.write(coord, textinrow)

        workbook.close()
        fh.close()

        for i in range(numxls):
            if i % 3 == 0:
                dupli = path + ''.join(
                    [random.choice(string.ascii_letters + string.digits) for n in range(randint(5, 15))]) + ".xlsx"
                dupli1 = path + ''.join(
                    [random.choice(string.ascii_letters + string.digits) for n in range(randint(5, 15))]) + ".txt"

                copyfile(name, dupli)
                copyfile(name1, dupli1)


def main():
    path = os.environ['USERPROFILE'] + "\\Desktop\\honey\\"

    if not os.path.exists(path):
        os.makedirs(path)

    randomxls(path)


if __name__ == '__main__':
    main()
