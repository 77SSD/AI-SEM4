import math
import random
import sys
import numpy as np
from copy import deepcopy
import time
toe = 300
ts = time.time()

s= sys.argv[1]
input_file = open(s, "r")
val = []
for line in input_file:
    m = len(line) - 1
    line = line[0:m]
    val.append(line)

type = val[0]
N = int(val[1])

coord = np.zeros((N, 2))
for i in range(2, N+2):
    temp = val[i].split()
    coord[i-2][0] = float(temp[0])
    coord[i-2][1] = float(temp[1])
# print(coord)

dist = np.zeros((N, N))
for i in range(N+2, 2*(N+1)):
    temp = val[i].split()
    for j in range(N):
        dist[i-(N+2)][j] = float(temp[j])
# print(dist)

def pathCost(path):
    SUM = 0
    for i in range(N-1):
        SUM+=dist[path[i]][path[i+1]]
    SUM+=dist[path[N-1]][path[0]]
    return SUM

def two_ex(path):
    bestP = path
    for i in range(N-1):
        if time.time() - ts > 300:
            return bestP, pathCost(bestP)
        for j in range(i+1, N):
            temp = deepcopy(path)
            temp[i+1:j+1] = np.flipud(temp[i+1:j+1])
            if pathCost(temp) < pathCost(bestP):
                bestP = temp
            if time.time() - ts > 300:
                return bestP, pathCost(bestP)
    return bestP, pathCost(bestP)

def moveGen(notAllowed, curr):
    prob = np.zeros([N])
    SUM = 0
    alpha = 1
    beta = 5
    for j in range(N):
        if j not in notAllowed:
            SUM = SUM + (((tau[curr][j])**alpha)*((eta[curr][j])**beta))
        j+=1
    for i in range(N):
        if i not in notAllowed:
            prob[i] = (((tau[curr][i])**alpha)*((eta[curr][i])**beta))/SUM
        i+=1
    return np.argmax(prob)

# if time.time() - ts > 300:
#     sys.exit()

def ACO():
    besttour = []
    best_path = []
    # iter = 20
    best_pathDist = math.inf
    # for z in range(iter):
    while(time.time() - ts < 225):
        path = np.zeros([ant_count, N], dtype = 'i')
        path[:, :] = -1
        pathDist = np.zeros(ant_count)
        comp = []
        i=0
        while i < ant_count:
            ins = random.randrange(0, N)
            if ins not in comp:
                comp.append(ins)
                path[i][0] = ins
                i+=1

        # print(path)
        for i in range(ant_count):
            for j in range(1, N):
                path[i][j] = moveGen(path[i], path[i][j-1])
                pathDist[i]+=dist[path[i][j-1]][path[i][j]]
            pathDist[i]+=dist[path[i][0]][path[i][N-1]]

        best_path = path[np.argmin(pathDist)]
        ze = min(pathDist)
        if best_pathDist > ze:
            best_pathDist = ze
            print("COST = ", best_pathDist)
            besttour = deepcopy(best_path)
            print("PATH = ", besttour)
            print("\n\n")

        # print(path)
        # print(best_path)
        # print(pathDist)
        # print("\n\n")

        for i in range(ant_count):
            for j in range(N):
                if j == N-1:
                    tau[path[i][j]][path[i][0]] = tau[path[i][j]][path[i][0]] + (Q/pathDist[i])
                    continue
                tau[path[i][j]][path[i][j+1]] = tau[path[i][j]][path[i][j+1]] + (Q/pathDist[i])
        
        for i in range(N):
            for j in range(N):
                tau[i][j] = (1-evapRate)*tau[i][j]
    return besttour, best_pathDist

    

eta = np.zeros((N, N))
for i in range(N):
    for j in range(N):
        if dist[i][j] == 0:
            eta[i][j] = math.inf
        else:
            eta[i][j] = 1/dist[i][j]

def greedy(groot):
    # groot = 99
    gtemp = np.copy(dist)
    curr = groot
    gpath = np.zeros((N), dtype = 'i')
    # print(gpath)
    gpath[0] = curr
    pathdist = 0
    gtemp[:, curr] = math.inf

    for i in range(1, N):
        min = np.min(gtemp[curr])
        pathdist += min
        curr = np.argmin(gtemp[curr])
        gpath[i] = curr
        gtemp[:, curr] = math.inf

    pathdist += dist[curr][groot]
    # return pathdist
    return gpath, pathdist

bgpath = []
bgpathDist = math.inf
for i in range(N):
    x, y = greedy(i)
    if bgpathDist > y:
        bgpath = x

tau = np.full((N, N), 0.1)
for i in range(N-1):
    tau[bgpath[i]][bgpath[i+1]]+=0.7
tau[bgpath[N-1]][0] += 0.7
ant_count = 15
evapRate = 0.0001
Q = 120
tour, best_pathDist = ACO()
# print(tour)
# print(best_pathDist)
tour, best_pathDist = two_ex(tour)
print("COST = ", best_pathDist)
print("PATH = ", tour)
print("\n\n")
if time.time() - ts > 300:
    exit()


print("Run completed in ", time.time()-ts,"sec")