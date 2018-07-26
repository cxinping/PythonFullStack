# -*- coding: utf-8 -*-

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题


# 生成画布
plt.figure(figsize=(8, 6), dpi=80)

# 打开交互模式
plt.ion()

# 循环
for index in range(100):
    # 清除原有图像
    plt.cla()

    # 设定标题等
    plt.title("动态曲线图")
    plt.grid(True)

    # 生成测试数据
    x = np.linspace(-np.pi + 0.1*index, np.pi+0.1*index, 256, endpoint=True)
    y_cos, y_sin = np.cos(x), np.sin(x)

    # 设置X轴
    plt.xlabel("X轴" )
    plt.xlim(-4 + 0.1*index, 4 + 0.1*index)
    plt.xticks(np.linspace(-4 + 0.1*index, 4+0.1*index, 9, endpoint=True))

    # 设置Y轴
    plt.ylabel("Y轴" )
    plt.ylim(-1.0, 1.0)
    plt.yticks(np.linspace(-1, 1, 9, endpoint=True))

    # 画两条曲线
    plt.plot(x, y_cos, "b--", linewidth=2.0, label="cos示例")
    plt.plot(x, y_sin, "g-", linewidth=2.0, label="sin示例")

    # 设置图例位置,loc可以为[upper, lower, left, right, center]
    plt.legend(loc="upper left",  shadow=True)

    # 暂停
    plt.pause(0.1)

# 关闭交互模式
plt.ioff()

# 图形显示
plt.show()
