# -*- coding: utf-8 -*-
import numpy as np
import datetime

# 路径设置
work_path = '/work/home/ackiec2x9h/lammps/Temperature/2-shock-nve/co2/1ns-1nm/'
input_file = open(work_path + 'shock', 'r')
output_file = open(work_path + 'press-teacher.txt', 'w')

# 参数设置
slic = 15     # 平滑窗口的一半
times = 2 * slic + 1  # 平滑总窗口数
MPA = 1.49    # 单位换算因子

# 读取所有原始行
lines = input_file.readlines()
atoms_number = int(lines[3].split()[0])
n_frames = int(len(lines) / (atoms_number + 9)) - 1

# 保存每一帧fz总力
fz_list = []

# 遍历每一帧，计算type 5原子的合力fz
for i in range(n_frames + 1):
    start = i * (atoms_number + 9) + 9
    end = (i + 1) * (atoms_number + 9)

    fz = 0
    for j in range(start, end):
        tmp = lines[j].split()
        if len(tmp) == 14 and tmp[2] == '5':
            fz += float(tmp[12])  # 第13列为fz
    fz_list.append(fz)

# 对fz进行滑动平均平滑
total_lines = len(fz_list)
for j in range(total_lines):
    star = j - slic
    end = j + slic + 1
    f = 0
    for k in range(star, end):
        adjusted_k = k % total_lines  # 周期边界处理
        f += fz_list[adjusted_k]
    data = f / times / MPA

    print(j, data)
    tmp1 = f"{j} {data:.6f}\n"
    output_file.write(tmp1)

# 关闭文件
input_file.close()
output_file.close()
