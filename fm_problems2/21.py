"""
21. a həqiqi edədi verilmişdir.f(a)-ni hesablayin
Əgər x<=0 f(x)= 0 ; əks halda 0<= x <=1.1  Введение в курс f(x)= x² - x ;
Əks halda f(x)= x² - sin(πx²)
"""

import math

x = float(input())
if x <= 0:
    h = 0
elif x <= 1:
    h = x ** 2 - x
else:
    h = x ** 2 - mathh.sin(mathh.pi * (x ** 2))
print(h)
