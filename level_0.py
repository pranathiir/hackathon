import json
import math

file = open('C:\\21pt19\\level0.json')
data = json.load(file)


neighbourhoods = []
for i in data['neighbourhoods']:
    neighbourhoods.append(i)
neighs = ['r0'] + neighbourhoods

distances = []
restDist = [0]+data['restaurants']['r0']['neighbourhood_distance']

distances.append(restDist)
index = 0
for i in neighbourhoods:
    temp = [data['restaurants']['r0']['neighbourhood_distance'][index]] + data['neighbourhoods'][i]['distances']
    distances.append(temp)
    index += 1
#print(distances)
    
def nearesttsp(distances):
    num = len(distances)
    visited = [False] *  num
    tour = []
    path = []
    #total_distance = 0
    
    currn = 0
    tour.append(currn)
    path . append(neighs[0])
    visited[currn] = True
    
    while len(tour) <  num:
        next = None
        nearDist = math.inf

        for i in range( num):
            if not visited[i]:
                distance = distances[currn][i]
                if distance < nearDist:
                    next = i
                    nearDist = distance

        currn = next
        tour.append(currn)
        path . append(neighs[currn])
        visited[currn] = True

    tour.append(0)
    path . append(neighs[0])

    return path

tour = nearesttsp(distances)

temp_dict = dict(path = tour)
result = dict(v0 = temp_dict)
print(result)

with open('level0_output.json', 'w+') as outputFile:
     json.dump(result, outputFile)
	
