# -*- coding: utf-8 -*-
"""Untitled20.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QanQ45r0HarBEPCgWXuf3D_dFqcp4q_O
"""

#area of regular polygon
from math import tan,pi
n=int(input('number of sides'))
s=int(input('length of any side'))
aorp=(n)*(s)**2/4*tan(pi/n)
print(aorp)