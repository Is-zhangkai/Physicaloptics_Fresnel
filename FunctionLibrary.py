# -*- coding: utf-8 -*-
# @Time    : 2022/9/19 16:02
# @Author  : zhangkai
# @File    : FunctionLibrary.py
# @Software: PyCharm
import numpy as np
import matplotlib.pyplot as plt


def jisuan(n_in, n_out, step_t=0.1):
    """
    Fresnel formula is used to calculate the transmission coefficient, reflection coefficient, transmission ratio and reflection ratio
    :param n_in:入射介质折射率
    :param n_out:介质折射率
    :param step_t: 0到90度的布局，默认为0.1，即900数据
    :return:
    """

    theta = np.arange(0 + step_t, 90 + step_t, step_t)  # 左闭右开，900数据
    theta1 = theta / 180 * np.pi

    # theta=np.arange(0.0000001,0.5*np.pi,0.1)

    # 计算折射角度
    sintheta = np.sin(theta1) * n_in / n_out
    # 全反射时
    sintheta[sintheta > 1] = 1
    theta2 = np.arcsin(sintheta)
    # 反射，透射系数计算
    rs = -np.sin(theta1 - theta2) / np.sin(theta1 + theta2)
    rp = np.tan(theta1 - theta2) / np.tan(theta1 + theta2)
    ts = 2 * np.cos(theta1) * np.sin(theta2) / np.sin(theta1 + theta2)
    tp = 2 * np.cos(theta1) * np.sin(theta2) / (np.sin(theta1 + theta2) * np.cos(theta1 - theta2))

    return theta, rs, rp, ts, tp

    # plt.plot(theta, rs,'r',label='rs')
    # plt.plot(theta, rp, 'g', label='ts')
    # plt.plot(theta, ts, 'b', label='rp')
    # plt.plot(theta, tp, 'y', label='tp')
    # plt.show()
    # print(thetaln)
