#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/3/23 18:27 
# @Author : Patrick 
# @File : pic2pdf.py 
# @Software: PyCharm


# import fitz
import os

import img2pdf


def pic2pdf():
    os.chdir('F:/Guitar/1Chords')
    for dir in os.listdir('F:/Guitar')[:]:
        if '.' in dir or 'Chords' in dir or 'Honesty' in dir:
            continue
        # print(dir)
        l = [os.path.join('F:/Guitar', dir, img) for img in os.listdir(os.path.join('F:/Guitar', dir))]
        # print(l)
        try:
            with open(dir + ".pdf", "wb") as f:
                f.write(img2pdf.convert(l))
        except Exception as e:
            print(dir + ' ERROR!')
        print(dir)


pic2pdf()
