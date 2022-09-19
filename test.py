# -*- coding: utf-8 -*-
# @Time    : 2022/9/19 18:27
# @Author  : zhangkai
# @File    : test.py
# @Software: PyCharm


import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    n1 = 1
    n2 = 1.5
    step_t = 10
    theta = np.arange(0 + step_t, 90 + step_t, step_t)  # 左闭右开，900数据
    thetaln = theta / 180 * np.pi
    # theta=np.arange(0.0000001,0.5*np.pi,0.1)
    sintheta = np.sin(thetaln) * n1 / n2
    sintheta[sintheta > 1] = 1  # 全反射
    theta2 = np.arcsin(sintheta)

    rs = -np.sin(thetaln - theta2) / np.sin(thetaln + theta2)
    rp = np.tan(thetaln - theta2) / np.tan(thetaln + theta2)
    ts = 2 * np.cos(thetaln) * np.sin(theta2) / np.sin(thetaln + theta2)
    tp = 2 * np.cos(thetaln) * np.sin(theta2) / (np.sin(thetaln + theta2) * np.cos(thetaln - theta2))
    plt.plot(theta, rs, 'r', label='rs')
    plt.plot(theta, rp, 'g', label='ts')
    plt.plot(theta, ts, 'b', label='rp')
    plt.plot(theta, tp, 'y', label='tp')
    plt.show()

    # print(thetaln)
