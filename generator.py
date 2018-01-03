#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 1 12:50:16 2018

@authors Rafael,Dmitriy
Ransomware Detection Project
Technion, Haifa, Israel

Auxiliary script for generating honepot-files with random names and content.
Currently, we generating *.txt, *.pdf, *.xlsx files.
"""

import os.path
import random
import string
from random import randint
from shutil import copyfile

import xlsxwriter
from fpdf import FPDF


# .xls Files
def randomxls(path):
    numxls = (randint(10, 20))

    for i in range(10):

        name = path + ''.join(
            [random.choice(string.ascii_letters + string.digits) for n in range(randint(5, 15))]) + ".xlsx"

        workbook = xlsxwriter.Workbook(name)
        worksheet = workbook.add_worksheet()

        numrows = (randint(10, 50))

        for i in range(numrows):
            coord = 'A' + str(i)

            textinrow = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(randint(5, 15))])

            worksheet.write(coord, textinrow)

        workbook.close()

        for i in range(numxls):
            dupli = path + ''.join(
                [random.choice(string.ascii_letters + string.digits) for n in range(randint(5, 15))]) + ".xlsx"

            copyfile(name, dupli)


# .pdf Files + .txt Files
def randompdf(path):
    numpdf = (randint(15, 20))

    for i in range(10):

        name = path + ''.join(
            [random.choice(string.ascii_letters + string.digits) for n in range(randint(5, 15))]) + ".pdf"
        name1 = path + ''.join(
            [random.choice(string.ascii_letters + string.digits) for n in range(randint(5, 15))]) + ".txt"
        fh = open(name1, "w+")

        numwords = (randint(10, 20))

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        words = []

        for i in range(numwords):
            randomword = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(randint(5, 15))])
            fh.write(randomword + "\n")
            words.append(randomword)

        fh.close()
        wordsinstring = ''.join(words)

        pdf.cell(200, 10, txt=wordsinstring, align="C")

        pdf.output(name)

        for i in range(numpdf):
            dupli = path + ''.join(
                [random.choice(string.ascii_letters + string.digits) for n in range(randint(5, 15))]) + ".pdf"
            dupli1 = path + ''.join(
                [random.choice(string.ascii_letters + string.digits) for n in range(randint(5, 15))]) + ".txt"

            copyfile(name, dupli)
            copyfile(name1, dupli1)


randomxls(os.environ['USERPROFILE'] + "\\Desktop\\honey\\")
randompdf(os.environ['USERPROFILE'] + "\\Desktop\\honey\\")
