import math

import numpy as np
def greedy100(m):
    
    count = 0

    point = [0,0]
    while True:
        count += 1
        up = [point[0],point[1]-1]
        down = [point[0],point[1]+1]
        left = [point[0]-1,point[1]]
        right = [point[0]+1,point[1]]
        points_value = [101]*5
        for point_around_id, point_around in enumerate([up,down,left,right]):
            if point_around[0]<0 or point_around[1]<0 or \
                        point_around[0]>99 or point_around[1]>99:
                continue
            points_value[point_around_id] = m[point_around[0],point_around[1]]
        points_value[4] = m[point[0],point[1]]
        if min(points_value) == points_value[4]:
            return count
        minid = points_value.index(min(points_value))
        point = [up,down,left,right][minid]

    

if __name__=="__main__":
    step_num=[]
    for i in range(10000):
        m = np.random.randint(1,100,size=(100,100))
        step_num.append(greedy100(m))
    print(sum(step_num))
    
    