# -*- coding: utf-8 -*-
import numpy as np
import datetime

work_path = '/work/home/ackiec2x9h/lammps/Temperature/2-shock-nve/co2/1ns-1nm/'
input_file = open(work_path + 'shock', 'r')  # 文件名

line = input_file.readlines()
atoms_number = int(line[3].split()[0])  ##那么split()会将这行分割成['3', 'atoms', '10', 'molecules']这个列表。split()[0]指这个列表的第一个元素，也就是'3'

sanwei_distribution = {}
x = 100
y = 100
z = 152
x1 = 4
y1 = 4
z1 = 4
slicx = 25
slicy = 25
slicz = 38


m_range = range(0, 505, 5)  # 从1到最后，隔十zhen算一次
for m in m_range:
    start = m * (atoms_number + 9) + 9
    end = (m + 1) * (atoms_number + 9)


    a = np.zeros(shape=(slicx * slicy * slicz, 4))
    n = 0
    for i in range(25):
        for l in range(25):
            for k in range(38):
                a[n, 0] = i + 1
                a[n, 1] = l + 1
                a[n, 2] = k + 1
                n += 1
    for n in range(start, end):
        # print(j)
        tmp = line[n].split()  # tmp【0】的数据类型为字符串
        pos_x = float(tmp[4])
        pos_y = float(tmp[5])
        pos_z = float(tmp[6])+11
        xnumber = 0
        ynumber = 0
        znumber = 0
        # print(y)
        if tmp[2] == "1" or tmp[2] == "2":   #'''tmp[2] == "3" or tmp[2] == "4": or '''
            for j in range(25):
                if j * x1 < pos_x <= j * x1 + x1:
                    xnumber = j
            for k in range(25):
                if k * y1 < pos_y <= k * y1 + y1:
                    ynumber = k
            for l in range(38):
                if l * z1 < pos_z <= l * z1 + z1:
                    znumber = l
            gezi = xnumber * slicy * slicz + ynumber * slicz + znumber + 1
            a[gezi - 1, 3] += 1
    z = float(m / 100)
    print(z)#对应时间ns
    np.savetxt(work_path + 'surface/H2O-1ns-1nm-' + str(m) + '.txt', a, fmt="%.3f")  # D:\pychart\practice
