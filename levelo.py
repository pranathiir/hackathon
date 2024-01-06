import json
import math

file = open('C:\\21pt19\\level0.json')
data = json.load(file)

dist = []
dictKeys = list(data.keys())
#print(dictKeys)
for i in dictKeys:
    if i == 'n_neighbourhoods':
        num = data["n_neighbourhoods"]
    #if i == 'neighbourhoods':

neigh = dict(data["neighbourhoods"])
neighs = list(data["neighbourhoods"])
for i in neighs:
    dist.append(neigh[i]["distances"])
#print(dist)

rest = dict(data["restaurants"])
r0 = list(rest["r0"]["neighbourhood_distance"])
#print(r0)

#print(neigh)
#print(neighs)
distances = {}
for keys in neighs:
    for values in dist:
        distances[keys] = values
        break
distances["r0"] = r0
print(len(distances))

def nearesttsp(distances):
    num = len(distances)
    visited = []
    cycle = []
    #total_distance = 0
    curr = 20
    currn = 'r0'
    cycle.append(currn)
    visited.append(curr)

    while len(cycle)<num:
        minm = 5000
        for n in range(num-1):
            if currn == 'r0':
                distance = distances[currn][n]
                if distance < minm and distance!=0:
                    minm = distance
                    next = n
            else:
                if n not in visited:
                    distance = distances[currn][n]
                    if distance < minm and distance!=0:
                        minm = distance
                        next = n
        currn = neighs[next]
        cycle.append(currn)
        curr = next
        #print(next)
        visited.append(curr)
        #print(visited)
        #total_distance += nearestDist

    #cycle.append(0)
#    total_distance += distances[curr][0]

    return cycle
cycle = nearesttsp(distances)
print("Tour:", cycle)