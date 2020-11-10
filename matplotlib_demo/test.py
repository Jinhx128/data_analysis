# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt


def show():
    x = range(2, 25, 2)

    y = [15, 13, 14, 5, 17, 20, 25, 26, 24, 22, 18, 15]

    plt.plot(x, y)
    plt.show()
