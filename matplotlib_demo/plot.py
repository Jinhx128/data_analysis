# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import random


def show():
    # 指定默认字体
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
    # 解决保存图像是负号'-'显示为方块的问题
    plt.rcParams['axes.unicode_minus'] = False

    plt.figure(figsize=(20, 8), dpi=200)

    x = range(120)

    random.seed(10)

    y_1 = [random.uniform(20, 35) for i in range(120)]
    y_2 = [random.uniform(20, 35) for i in range(120)]

    # 折线图
    plt.plot(x, y_1, label='111哈哈哈', linestyle='--', color='blue', alpha=0.5)
    plt.plot(x, y_2, label='222呵呵呵', linestyle='-', color='purple', alpha=0.5)

    # 修改位置，默认右上角
    plt.legend(loc='best')

    _x_ticks = ['10点{}分'.format(i) for i in x if i < 60]
    _x_ticks += ['11点{}分'.format(i) for i in x if i < 60]

    plt.title('这里是标题！！！')
    plt.xlabel('y轴含义！！！')
    plt.ylabel('x轴含义！！！')

    plt.grid(alpha=0.4)

    plt.xticks(x[::5], _x_ticks[::5], rotation=45)

    # plt.savefig('matplotlib_demo/file/plot.png')

    plt.show()

