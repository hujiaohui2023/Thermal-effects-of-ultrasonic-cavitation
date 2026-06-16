# -*- coding: utf-8 -*-
import numpy as np
import  datetime

work_path='/work/home/ackiec2x9h/lammps/Temperature/2-shock-nve/1ns-1nm/'  #/work/home/ackiec2x9h/lammps/Temperature/2-shock-nve/1ns-2nm
input_file=open(work_path+'shock','r') #文件名
output_file=open(work_path+'number-shock.txt','w')

lines=input_file.readlines()
atoms_number=int(lines[3].split()[0])
n_frames=int(len(lines)/(atoms_number+9))-1
n_CO2 = 0
n_H2O = 0
cut_off=4 #截断距离
cut_number1=3
cut_number2=0

n_CO2 = 733
n_H2O = 24604
ii=0
i_range=range(0,505,5)#从1到最后，隔十zhen算一次
for i in i_range:
    ii+=1
    start=i*(atoms_number+9)+9
    end=(i+1)*(atoms_number+9)
    CO2 = np.zeros(shape=(n_CO2, 3))
    H2O = np.zeros(shape=(n_H2O, 3))
    id_CO2 = 0
    id_H2O = 0
    for j in range(start,end):
        tmp = lines[j].split()
        if len(tmp)==13:
            if tmp[2]=='3':
                CO2[id_CO2:id_CO2+1,0:1]=float(tmp[4])
                CO2[id_CO2:id_CO2+1,1:2]=float(tmp[5])
                CO2[id_CO2:id_CO2+1,2:3]=float(tmp[6])
                id_CO2+=1
            elif tmp[2]=='1':
                H2O[id_H2O:id_H2O+1,0:1]=float(tmp[4])
                H2O[id_H2O:id_H2O+1,1:2]=float(tmp[5])
                H2O[id_H2O:id_H2O+1,2:3]=float(tmp[6])
                id_H2O+=1
    CO2_H2O = np.zeros(shape=(n_CO2, 2))
    for c in range(len(CO2)):
        pos_co2=CO2[c:c+1]
        n_range=0
        for h in range(len(H2O)):
            pos_h2o=H2O[h:h+1]
            deta=pos_co2-pos_h2o
            long=np.linalg.norm(deta)
            if long<cut_off:
                n_range+=1
        CO2_H2O[c:c+1,0:1]=c
        CO2_H2O[c:c+1,1:2]=n_range
    n_in = 0
    n_out = 0
    n_sur = 0
    for n in range(len(CO2)):
        nn=CO2_H2O[n:n + 1, 1:2]
        if nn>cut_number1:
            n_out+=1
        elif cut_number2<nn<=cut_number1:
            n_sur+=1
        else :
            n_in+=1
    tmp=str(i)+' '+str(n_in)+' '+str(n_sur)+' '+str(n_out)+'\n'
    output_file.write(tmp)
output_file.close()
