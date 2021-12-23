# -*- coding: utf-8 -*-
"""
aimfunc.py - 目标函数文件
描述:
    目标：max f = 21.5 + x1 * np.sin(4 * np.pi * x1) + x2 * np.sin(20 * np.pi * x2)
    约束条件：
        x1 != 10
        x2 != 5
        x1 ∈ [-3, 12.1] # 变量范围是写在遗传算法的参数设置里面
        x2 ∈ [4.1, 5.8]
"""

import numpy as np
# 大批量15个数据
# 1180,1177,1161,1158,1079,1048,1022,994,948,900,831,765,731,712,611
# 小批量24个数据
# 586,553,546,513,509,469,431,430,429,426,417,416,387,350,318,317,286,207,201,182,177,162,127,73

BT1=np.array([1022,994,948,900,831,765,731,712,611,1180,1177,1161,1158,1079,1048])
BT2=np.array([416,387,350,318,317,286,207,201,182,177,162,127,73,586,553,546,513,509,469,431,430,429,426,417])




processtime_for_one_product = 30
setuptime = 1800

def aimfunc(Phen, CV):
    x1 = Phen[:, [0]]
    x2 = Phen[:, [1]]
    x3 = Phen[:, [2]]
    x4 = Phen[:, [3]]
    x5 = Phen[:, [4]]
    x6 = Phen[:, [5]]
    x7 = Phen[:, [6]]
    x8 = Phen[:, [7]]
    x9 = Phen[:, [8]]
    x10 = Phen[:, [9]]
    x11 = Phen[:, [10]]
    x12 = Phen[:, [11]]
    x13 = Phen[:, [12]]
    x14 = Phen[:, [13]]
    x15 = Phen[:, [14]]
    x16 = Phen[:, [15]]
    x17 = Phen[:, [16]]
    x18 = Phen[:, [17]]
    x19 = Phen[:, [18]]
    x20 = Phen[:, [19]]
    x21 = Phen[:, [20]]
    x22 = Phen[:, [21]]
    x23 = Phen[:, [22]]
    x24 = Phen[:, [23]]
    x25 = Phen[:, [24]]
    x26 = Phen[:, [25]]
    x27 = Phen[:, [26]]
    x28 = Phen[:, [27]]
    x29 = Phen[:, [28]]
    x30 = Phen[:, [29]]
    x31 = Phen[:, [30]]
    x32 = Phen[:, [31]]
    x33 = Phen[:, [32]]
    x34 = Phen[:, [33]]
    x35 = Phen[:, [34]]
    x36 = Phen[:, [35]]
    x37 = Phen[:, [36]]
    x38 = Phen[:, [37]]
    x39 = Phen[:, [38]]
    x40 = Phen[:, [39]]
    x41 = Phen[:, [40]]
    x42 = Phen[:, [41]]
    x43 = Phen[:, [42]]
    x44 = Phen[:, [43]]
    x45 = Phen[:, [44]]
    y1 = Phen[:, [45]]
    y2 = Phen[:, [46]]
    y3 = Phen[:, [47]]
    y4 = Phen[:, [48]]
    y5 = Phen[:, [49]]
    y6 = Phen[:, [50]]
    y7 = Phen[:, [51]]
    y8 = Phen[:, [52]]
    y9 = Phen[:, [53]]
    y10 = Phen[:, [54]]
    y11 = Phen[:, [55]]
    y12 = Phen[:, [56]]
    y13 = Phen[:, [57]]
    y14 = Phen[:, [58]]
    y15 = Phen[:, [59]]
    y16 = Phen[:, [60]]
    y17 = Phen[:, [61]]
    y18 = Phen[:, [62]]
    y19 = Phen[:, [63]]
    y20 = Phen[:, [64]]
    y21 = Phen[:, [65]]
    y22 = Phen[:, [66]]
    y23 = Phen[:, [67]]
    y24 = Phen[:, [68]]
    y25 = Phen[:, [69]]
    y26 = Phen[:, [70]]
    y27 = Phen[:, [71]]
    y28 = Phen[:, [72]]
    y29 = Phen[:, [73]]
    y30 = Phen[:, [74]]
    y31 = Phen[:, [75]]
    y32 = Phen[:, [76]]
    y33 = Phen[:, [77]]
    y34 = Phen[:, [78]]
    y35 = Phen[:, [79]]
    y36 = Phen[:, [80]]
    y37 = Phen[:, [81]]
    y38 = Phen[:, [82]]
    y39 = Phen[:, [83]]
    y40 = Phen[:, [84]]
    y41 = Phen[:, [85]]
    y42 = Phen[:, [86]]
    y43 = Phen[:, [87]]
    y44 = Phen[:, [88]]
    y45 = Phen[:, [89]]
    y46 = Phen[:, [90]]
    y47 = Phen[:, [91]]
    y48 = Phen[:, [92]]
    y49 = Phen[:, [93]]
    y50 = Phen[:, [94]]
    y51 = Phen[:, [95]]
    y52 = Phen[:, [96]]
    y53 = Phen[:, [97]]
    y54 = Phen[:, [98]]
    y55 = Phen[:, [99]]
    y56 = Phen[:, [100]]
    y57 = Phen[:, [101]]
    y58 = Phen[:, [102]]
    y59 = Phen[:, [103]]
    y60 = Phen[:, [104]]
    y61 = Phen[:, [105]]
    y62 = Phen[:, [106]]
    y63 = Phen[:, [107]]
    y64 = Phen[:, [108]]
    y65 = Phen[:, [109]]
    y66 = Phen[:, [110]]
    y67 = Phen[:, [111]]
    y68 = Phen[:, [112]]
    y69 = Phen[:, [113]]
    y70 = Phen[:, [114]]
    y71 = Phen[:, [115]]
    y72 = Phen[:, [116]]

    f = x1 * (BT1[0] * processtime_for_one_product + setuptime) + \
               x2 * (BT1[1] * processtime_for_one_product + setuptime) + \
               x3 * (BT1[2] * processtime_for_one_product + setuptime) + \
               x4 * (BT1[3] * processtime_for_one_product + setuptime) + \
               x5 * (BT1[4] * processtime_for_one_product + setuptime) + \
               x6 * (BT1[5] * processtime_for_one_product + setuptime) + \
               x7 * (BT1[6] * processtime_for_one_product + setuptime) + \
               x8 * (BT1[7] * processtime_for_one_product + setuptime) + \
               x9 * (BT1[8] * processtime_for_one_product + setuptime) + \
               x10 * (BT1[9] * processtime_for_one_product + setuptime) + \
               x11 * (BT1[10] * processtime_for_one_product + setuptime) + \
               x12 * (BT1[11] * processtime_for_one_product + setuptime) + \
               x13 * (BT1[12] * processtime_for_one_product + setuptime) + \
               x14 * (BT1[13] * processtime_for_one_product + setuptime) + \
               x15 * (BT1[14] * processtime_for_one_product + setuptime) + \
               x16 * (BT1[0] * processtime_for_one_product + setuptime) + \
               x17 * (BT1[1] * processtime_for_one_product + setuptime) + \
               x18 * (BT1[2] * processtime_for_one_product + setuptime) + \
               x19 * (BT1[3] * processtime_for_one_product + setuptime) + \
               x20 * (BT1[4] * processtime_for_one_product + setuptime) + \
               x21 * (BT1[5] * processtime_for_one_product + setuptime) + \
               x22 * (BT1[6] * processtime_for_one_product + setuptime) + \
               x23 * (BT1[7] * processtime_for_one_product + setuptime) + \
               x24 * (BT1[8] * processtime_for_one_product + setuptime) + \
               x25 * (BT1[9] * processtime_for_one_product + setuptime) + \
               x26 * (BT1[10] * processtime_for_one_product + setuptime) + \
               x27 * (BT1[11] * processtime_for_one_product + setuptime) + \
               x28 * (BT1[12] * processtime_for_one_product + setuptime) + \
               x29 * (BT1[13] * processtime_for_one_product + setuptime) + \
               x30 * (BT1[14] * processtime_for_one_product + setuptime) + \
               x31 * (BT1[0] * processtime_for_one_product + setuptime) + \
               x32 * (BT1[1] * processtime_for_one_product + setuptime) + \
               x33 * (BT1[2] * processtime_for_one_product + setuptime) + \
               x34 * (BT1[3] * processtime_for_one_product + setuptime) + \
               x35 * (BT1[4] * processtime_for_one_product + setuptime) + \
               x36 * (BT1[5] * processtime_for_one_product + setuptime) + \
               x37 * (BT1[6] * processtime_for_one_product + setuptime) + \
               x38 * (BT1[7] * processtime_for_one_product + setuptime) + \
               x39 * (BT1[8] * processtime_for_one_product + setuptime) + \
               x40 * (BT1[9] * processtime_for_one_product + setuptime) + \
               x41 * (BT1[10] * processtime_for_one_product + setuptime) + \
               x42 * (BT1[11] * processtime_for_one_product + setuptime) + \
               x43 * (BT1[12] * processtime_for_one_product + setuptime) + \
               x44 * (BT1[13] * processtime_for_one_product + setuptime) + \
               x45 * (BT1[14] * processtime_for_one_product + setuptime) + \
               y1 * (BT2[0] * processtime_for_one_product + setuptime) + \
               y2 * (BT2[1] * processtime_for_one_product + setuptime) + \
               y3 * (BT2[2] * processtime_for_one_product + setuptime) + \
               y4 * (BT2[3] * processtime_for_one_product + setuptime) + \
               y5 * (BT2[4] * processtime_for_one_product + setuptime) + \
               y6 * (BT2[5] * processtime_for_one_product + setuptime) + \
               y7 * (BT2[6] * processtime_for_one_product + setuptime) + \
               y8 * (BT2[7] * processtime_for_one_product + setuptime) + \
               y9 * (BT2[8] * processtime_for_one_product + setuptime) + \
               y10 * (BT2[9] * processtime_for_one_product + setuptime) + \
               y11 * (BT2[10] * processtime_for_one_product + setuptime) + \
               y12 * (BT2[11] * processtime_for_one_product + setuptime) + \
               y13 * (BT2[12] * processtime_for_one_product + setuptime) + \
               y14 * (BT2[13] * processtime_for_one_product + setuptime) + \
               y15 * (BT2[14] * processtime_for_one_product + setuptime) + \
               y16 * (BT2[15] * processtime_for_one_product + setuptime) + \
               y17 * (BT2[16] * processtime_for_one_product + setuptime) + \
               y18 * (BT2[17] * processtime_for_one_product + setuptime) + \
               y19 * (BT2[18] * processtime_for_one_product + setuptime) + \
               y20 * (BT2[19] * processtime_for_one_product + setuptime) + \
               y21 * (BT2[20] * processtime_for_one_product + setuptime) + \
               y22 * (BT2[21] * processtime_for_one_product + setuptime) + \
               y23 * (BT2[22] * processtime_for_one_product + setuptime) + \
               y24 * (BT2[23] * processtime_for_one_product + setuptime) + \
               y25 * (BT2[0] * processtime_for_one_product + setuptime) + \
               y26 * (BT2[1] * processtime_for_one_product + setuptime) + \
               y27 * (BT2[2] * processtime_for_one_product + setuptime) + \
               y28 * (BT2[3] * processtime_for_one_product + setuptime) + \
               y29 * (BT2[4] * processtime_for_one_product + setuptime) + \
               y30 * (BT2[5] * processtime_for_one_product + setuptime) + \
               y31 * (BT2[6] * processtime_for_one_product + setuptime) + \
               y32 * (BT2[7] * processtime_for_one_product + setuptime) + \
               y33 * (BT2[8] * processtime_for_one_product + setuptime) + \
               y34 * (BT2[9] * processtime_for_one_product + setuptime) + \
               y35 * (BT2[10] * processtime_for_one_product + setuptime) + \
               y36 * (BT2[11] * processtime_for_one_product + setuptime) + \
               y37 * (BT2[12] * processtime_for_one_product + setuptime) + \
               y38 * (BT2[13] * processtime_for_one_product + setuptime) + \
               y39 * (BT2[14] * processtime_for_one_product + setuptime) + \
               y40 * (BT2[15] * processtime_for_one_product + setuptime) + \
               y41 * (BT2[16] * processtime_for_one_product + setuptime) + \
               y42 * (BT2[17] * processtime_for_one_product + setuptime) + \
               y43 * (BT2[18] * processtime_for_one_product + setuptime) + \
               y44 * (BT2[19] * processtime_for_one_product + setuptime) + \
               y45 * (BT2[20] * processtime_for_one_product + setuptime) + \
               y46 * (BT2[21] * processtime_for_one_product + setuptime) + \
               y47 * (BT2[22] * processtime_for_one_product + setuptime) + \
               y48 * (BT2[23] * processtime_for_one_product + setuptime) + \
               y49 * (BT2[0] * processtime_for_one_product + setuptime) + \
               y50 * (BT2[1] * processtime_for_one_product + setuptime) + \
               y51 * (BT2[2] * processtime_for_one_product + setuptime) + \
               y52 * (BT2[3] * processtime_for_one_product + setuptime) + \
               y53 * (BT2[4] * processtime_for_one_product + setuptime) + \
               y54 * (BT2[5] * processtime_for_one_product + setuptime) + \
               y55 * (BT2[6] * processtime_for_one_product + setuptime) + \
               y56 * (BT2[7] * processtime_for_one_product + setuptime) + \
               y57 * (BT2[8] * processtime_for_one_product + setuptime) + \
               y58 * (BT2[9] * processtime_for_one_product + setuptime) + \
               y59 * (BT2[10] * processtime_for_one_product + setuptime) + \
               y60 * (BT2[11] * processtime_for_one_product + setuptime) + \
               y61 * (BT2[12] * processtime_for_one_product + setuptime) + \
               y62 * (BT2[13] * processtime_for_one_product + setuptime) + \
               y63 * (BT2[14] * processtime_for_one_product + setuptime) + \
               y64 * (BT2[15] * processtime_for_one_product + setuptime) + \
               y65 * (BT2[16] * processtime_for_one_product + setuptime) + \
               y66 * (BT2[17] * processtime_for_one_product + setuptime) + \
               y67 * (BT2[18] * processtime_for_one_product + setuptime) + \
               y68 * (BT2[19] * processtime_for_one_product + setuptime) + \
               y69 * (BT2[20] * processtime_for_one_product + setuptime) + \
               y70 * (BT2[21] * processtime_for_one_product + setuptime) + \
               y71 * (BT2[22] * processtime_for_one_product + setuptime) + \
               y72 * (BT2[23] * processtime_for_one_product + setuptime) - 1800


    CV = np.hstack([
        np.abs(x1 + x16 + x31 - 1), np.abs(x2 + x17 + x32 - 1),
        np.abs(x3 + x18 + x33 - 1), np.abs(x4 + x19 + x34 - 1),
        np.abs(x5 + x20 + x35 - 1), np.abs(x6 + x21 + x36 - 1),
        np.abs(x7 + x22 + x37 - 1), np.abs(x8 + x23 + x38 - 1),
        np.abs(x9 + x24 + x39 - 1), np.abs(x10 + x25 + x40 - 1),
        np.abs(x11 + x26 + x41 - 1), np.abs(x12 + x27 + x42 - 1),
        np.abs(x13 + x28 + x43 - 1), np.abs(x14 + x29 + x44 - 1),
        np.abs(x15 + x30 + x45 - 1), np.abs(y1 + y25 + y49 - 1),
        np.abs(y2 + y26 + y50 - 1), np.abs(y3 + y27 + y51 - 1),
        np.abs(y4 + y28 + y52 - 1), np.abs(y5 + y29 + y53 - 1),
        np.abs(y6 + y30 + y54 - 1), np.abs(y7 + y31 + y55 - 1),
        np.abs(y8 + y32 + y56 - 1), np.abs(y9 + y33 + y57 - 1),
        np.abs(y10 + y34 + y58 - 1), np.abs(y11 + y35 + y59 - 1),
        np.abs(y12 + y36 + y60 - 1), np.abs(y13 + y37 + y61 - 1),
        np.abs(y14 + y38 + y62 - 1), np.abs(y15 + y39 + y63 - 1),
        np.abs(y16 + y40 + y64 - 1), np.abs(y17 + y41 + y65 - 1),
        np.abs(y18 + y42 + y66 - 1), np.abs(y19 + y43 + y67 - 1),
        np.abs(y20 + y44 + y68 - 1), np.abs(y21 + y45 + y69 - 1),
        np.abs(y22 + y46 + y70 - 1), np.abs(y23 + y47 + y71 - 1),
        np.abs(y24 + y48 + y72 - 1)
    ])
    return [f, CV]

