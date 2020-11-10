# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import random


def show():
    # 指定默认字体
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
    # 解决保存图像是负号'-'显示为方块的问题
    plt.rcParams['axes.unicode_minus'] = False

    plt.figure(figsize=(20, 8), dpi=200)

    random.seed(10)

    x = ["战狼2", "速度与激情8", "功夫瑜伽", "西游伏妖篇", "变形金刚5：最后的骑士", "摔跤吧！爸爸", "加勒比海盗5：死无对证", "金刚：骷髅岛", "极限特工：终极回归", "生化危机6：终章",
         "乘风破浪", "神偷奶爸3", "智取威虎山", "大闹天竺", "金刚狼3：殊死一战", "蜘蛛侠：英雄归来", "悟空传", "银河护卫队2", "情圣", "新木乃伊", ]

    y_1 = [random.uniform(1, 100) for i in range(20)]

    y_2 = [random.uniform(1, 100) for i in range(20)]

    y_3 = [random.uniform(1, 100) for i in range(20)]

    x_cont = range(len(x))

    bar_width = 0.2

    # 折线图
    plt.bar(x_cont, y_1, width=bar_width, label='111哈哈哈', linestyle='--', color='blue', alpha=0.5)
    plt.bar([i + bar_width for i in x_cont], y_2, width=bar_width, label='222哈哈哈', linestyle='--', color='red', alpha=0.5)
    plt.bar([i + bar_width * 2 for i in x_cont], y_3, width=bar_width, label='333哈哈哈', linestyle='--', color='green', alpha=0.5)

    # 修改位置，默认右上角
    plt.legend(loc='best')

    plt.title('这里是标题！！！')
    plt.xlabel('y轴含义！！！')
    plt.ylabel('x轴含义！！！')

    plt.grid(alpha=0.4)

    plt.xticks([i + bar_width for i in x_cont], x, rotation=45)

    plt.savefig('matplotlib_demo/file/bar.png')

    plt.show()

