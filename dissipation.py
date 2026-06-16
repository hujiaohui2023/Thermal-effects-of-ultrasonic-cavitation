# -*- coding: utf-8 -*-
import numpy as np
import math
import datetime

# 路径设置
work_path = '/work/home/ackiec2x9h/lammps/Temperature/2-shock-nve/co2/1ns-1nm/'
#input_file = open(work_path + 'shock', 'r')
output_file = open(work_path + 'dissipation-viscous.txt', 'w')

# 参数设置
mu = 0.0008		# 水的μ，300 K

A = 1e-9      # 振幅 1 nm
S = 1e-16
all_V = S*A

dt = 1e-11
T = 1e-9      # 周期 1 ns
omega = 2 * math.pi / T   # 角频率

data = np.loadtxt(work_path + "surface.txt", dtype=str)
# 清理方括号并转换为浮点数
data = np.array([[float(x.replace('[', '').replace(']', '')) for x in row] for row in data])
R_list = data[:, 6]  # 第 7 列是 radiu
total_dissipation = 0.0

for i in range(len(data)):
  t = i * dt
  dVdt = omega * all_V * math.cos(omega * t)
  R = R_list[i] * 1e-10	#V = data[:, 4]
  Q = mu * (dVdt**2) / (math.pi * R**3)			# 粘性耗散功率
  total_dissipation += Q * dt
  tmp = f"{5*i} {Q} {total_dissipation}\n"
  output_file.write(tmp)
output_file.close()		# 关闭文件