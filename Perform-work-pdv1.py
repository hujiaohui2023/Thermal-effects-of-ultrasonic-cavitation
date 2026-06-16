# -*- coding: utf-8 -*-
import numpy as np
import math
import datetime

work_path = '/work/home/ackiec2x9h/lammps/Temperature/2-shock-nve/co2/1ns-1nm/'
output_file = open(work_path + 'perform1.txt', 'w')

# 参数设置
kB = 1.38e-23  # 玻尔兹曼常数 (J/K)
number = 3665  # 粒子数（CO2系统）

A = 1e-9      # 振幅 1 nm
S = 1e-16
all_V = S*A
dt = 1e-11
T = 1e-9      # 周期 1 ns
omega = 2 * math.pi / T   # 角频率

cumulative_work = 0  # 累计功 (J)

data = np.loadtxt(work_path + 'press-teacher.txt') 
data1 = np.loadtxt(work_path + 'banjing.txt') 

for i in range(len(data1)):
    pressure = data[i*5, 1] * 1e6  # Pa
    r = data1[i, 1] * 1e-10
    pressure1 = ( pressure + 2*0.072/r )
    t = i * 5 * dt
    dVdt = omega * all_V * math.cos(omega * t)
    # 计算功增量 dW = P * (dV/dt，根据理论公式计算) * dt
    dW = pressure1 * dVdt * dt
    
    # 每100步重置累计功（可选）
    #if i % 100 == 0:
        #cumulative_work = 0
    
    cumulative_work += dW
    
    # 计算温度（假设功全部转化为热能）
    temperature = (2.0 * cumulative_work) / (number * kB) + 260  # 初始温度272K
    
    # 输出结果
    print(i, temperature)
    output_file.write(f"{i} {cumulative_work} {temperature}\n")

output_file.close()