import numpy as np
work_path = '/work/home/ackiec2x9h/lammps/Temperature/2-shock-nve/co2/1ns-1nm/'
output_file=open(work_path+'surface.txt','w')

m_range = range(0, 405, 5)
nn=0
for m in m_range:
    z = float(m / 200)
    a=np.loadtxt(work_path+'surface/H2O-1ns-1nm-' + str(m) + '.txt')
    distance=0
    list=[]
    list1=[]
    number=0
    nn+=1
    list2=[]
    boundry1=0
    boundry=0

    for i in range(len(a)):
        if a[i:i+1,3:4]>0:
            boundry1=a[i:i+1,2:3]
            list2.append(boundry1)
            boundry = max(list2)


    for p in range(len(a)):
        if a[p, 2] <= boundry-1 and a[p,3] <=2:
            list.append(p)

    for p in list:
        o=0
        pos1=a[p:p+1,:3]
        for q in list:
            pos2=a[q:q+1,:3]
            distance=np.linalg.norm(pos1-pos2)
            if distance <= pow(3,1/2):
                o+=1

        if o>4:
            number+=1
            list1.append(p)

    volume=64*number
    volume1=3 * volume / (4 * np.pi)
    radius = pow(volume1,(1/3))  #radius = (3 * volume / (4 * np.pi)) ** (1/3)
    surface_area = 4 * np.pi * pow(radius,2)

    tmp =str(m)+' '+str(boundry)+' '+str(number)+' '+str(radius)+' '+str(volume)+' '+str(surface_area)+'\n'
    output_file.write(tmp)


    b = np.zeros(shape=(len(list1), 3))
    n = 0
    for i in list1:
        b[n, :3] = a[i, :3]
        n += 1
    np.savetxt(work_path + 'surface/H2O-1ns-1nm-' + str(m) + '-1.txt', b, fmt="%d")
output_file.close()

