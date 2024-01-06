import sys
import json
import math

file = open('C:\\21pt19\\level1a.json')
data = json.load(file)

neighs = data["neighbourhoods"]
restaurant = data["restaurants"]["r0"]
maxCapacity = data["vehicles"]["v0"]["capacity"]

def nearest(neighs, restaurant, maxCapacity):
    capacity = 0
    currn = "r0"
    visited = set()
    paths = {}

    while len(visited) < data["n_neighbourhoods"]:
        minm = sys.maxsize
        next = None

        for neighbor, orders in neighs.items():
            #print(neighbor)
            #print(orders)
            if neighbor not in visited and capacity + orders["order_quantity"] <= maxCapacity:
                dist = restaurant["neighbourhood_distance"][int(neighbor[1:])]
                if dist < minm:
                    minm = dist
                    next = neighbor
                    #print(next)

        if next:
            if currn not in paths:
                paths[currn] = [currn]

            paths[currn].append(next)
            capacity += neighs[next]["order_quantity"]
            visited.add(next)
            currn = next
        else:
            capacity = 0
            currn = "r0"
            
    print(paths)
    if currn not in paths:
        paths[currn] = [currn, "r0"]
    else:
        paths[currn].append("r0")

    return paths

paths = nearest(neighs, restaurant, maxCapacity)
output = {}
for i, (key, path) in enumerate(paths.items()):
    output[f"path{i+1}"] = path

print(output)

#print(output)
finalop = {}
finalop["v0"] = output
with open('C:\\21pt19\\level1a_output.json', 'w+') as outputFile:
     json.dump(finalop, outputFile)