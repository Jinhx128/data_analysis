# -*- coding: utf-8 -*-
import numpy as np
import random

def show():
    a = np.arange(1, 6)
    print(a)
    print(a.dtype)
    print(type(a))
    print("*"*100)

    b = np.array(range(1, 6), dtype='i1')
    print(b)
    print(b.dtype)
    print(type(b))
    print("*" * 100)

    c = np.array([1, 0, 1, 0, 1, ], dtype=bool)
    print(c)
    print(c.dtype)
    print(type(c))
    print("*" * 100)

    d = c.astype('i8')
    print(d)
    print(d.dtype)
    print(type(d))
    print("*" * 100)

    e = np.array([random.random() for i in range(10)])
    print(e)
    print("*" * 100)

    f = np.round(e, 3)
    print(f)
    print("*" * 100)