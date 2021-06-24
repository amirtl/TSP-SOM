import math, sys, random
import matplotlib.pyplot as plt



def Scale(coordinates):
    min1 = sys.maxsize
    max1 = -1
    min2 = sys.maxsize
    max2 = -1
    for i in coordinates:
        if i[0] < min1:
            min1 =i[0]
        if i[0] > max1:
            max1 = i[0]
        if i[1] < min2:
            min2 =i[1]
        if i[1] > max2:
            max2 = i[1]
    
    diff1 = max1 - min1
    diff2 = max2 - min2
    for i in range(len(coordinates)):
        coordinates[i] = ((coordinates[i][0] - min1)/diff1, (coordinates[i][1] - min2)/diff2)
    
    return diff1, diff2, min1, min2


def ReScale(diff1, diff2, min1, min2, coordinates):
    for i in range(len(coordinates)):
        coordinates[i] = (coordinates[i][0]*diff1+min1, coordinates[i][1]*diff2+min2, coordinates[i][2])


def distance(x,y):
    return math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)


def Find_Winner(x, w_coordinates):
    min = sys.maxsize
    index = -1
    for i in range(len(w_coordinates)):
        dist = distance(x , w_coordinates[i])
        if dist < min:
            min = dist
            index = i
        
    return index


def Initial(w_coordinates, size, radius):
    i = 0
    numb = 0
    while i < 2*math.pi:
        w_coordinates.append((0.5 + math.cos(i) * radius, 0.5+math.sin(i) * radius, numb))
        i += 2*math.pi/size
        numb += 1


def Find_Neighbors(w_coordinates, w, R):
    neighbors = []
    for i in range(len(w_coordinates)):
        if distance(w, w_coordinates[i]) <= R:
            neighbors.append(i)
    
    return neighbors


def Length(w_coordinates):
    dist = 0
    for i in range(len(w_coordinates)-1):
        dist += distance(w_coordinates[i], w_coordinates[i+1])
    dist += distance(w_coordinates[0], w_coordinates[len(w_coordinates)-1])
    
    return dist


def Is_New(Gene, city):
    for c in Gene:
        if c == city:
            return False
    
    return True


def Path(coordinates, w_coordinates):
    path = []
    for i in range(len(coordinates)):
        near = Find_Winner(coordinates[i], w_coordinates)
        path.append(w_coordinates[near])
    path.sort(key = lambda x: x[2])
    
    return path


def SOM(coordinates, size, R, alpha, numb_iter):
    diff1, diff2, min1, min2 = Scale(coordinates)
    w_coordinates = []
    Initial(w_coordinates, 2*size, 0.5)
    for i in range(numb_iter):
        j = random.randint(0,size-1)
        winner = Find_Winner(coordinates[j], w_coordinates)
        neighbors = Find_Neighbors(w_coordinates, w_coordinates[winner], R)
        for k in range(len(neighbors)):
            w_coordinates[neighbors[k]] = (w_coordinates[neighbors[k]][0] + alpha*(coordinates[j][0] - w_coordinates[neighbors[k]][0]), w_coordinates[neighbors[k]][1] + alpha*(coordinates[j][1] - w_coordinates[neighbors[k]][1]), w_coordinates[neighbors[k]][2])
        if i % 10 == 0:    
            R /= 2

    ReScale(diff1, diff2, min1, min2, w_coordinates)
    return w_coordinates


size = 29
coordinates = [(1150.0, 1760.0),
            (630.0 ,  1660.0),
            (40.0  ,  2090.0),
            (750.0 ,  1100.0),
            (750.0 ,  2030.0),
            (1030.0,  2070.0),
            (1650.0,  650.0 ),
            (1490.0,  1630.0),
            (790.0 ,  2260.0),
            (710.0 ,  1310.0),
            (840.0 ,  550.0 ),
            (1170.0,  2300.0),
            (970.0 ,  1340.0),
            (510.0 ,  700.0 ),
            (750.0 ,  900.0 ),
            (1280.0,  1200.0),
            (230.0 ,  590.0 ),
            (460.0 ,  860.0 ),
            (1040.0,  950.0 ),
            (590.0 ,  1390.0),
            (830.0 ,  1770.0),
            (490.0 ,  500.0 ),
            (1840.0,  1240.0),
            (1260.0,  1500.0),
            (1280.0,  790.0 ),
            (490.0 ,  2130.0),
            (1460.0,  1420.0),
            (1260.0,  1910.0),
            (360.0 ,  1980.0),
        ]

R = 0.3
alpha = 0.2
numb_iter = 10000
best = sys.maxsize
w_coordinates = SOM(coordinates[:], size, R, alpha, numb_iter)
path = Path(coordinates, w_coordinates)
print("Length: ")
print(Length(path))

x= []
y = []
w = path
for i in w:
    x.append(i[0])
    y.append(i[1])

x.append(w[0][0])
y.append(w[0][1])
plt.plot(x, y)

x= []
y = []
w = coordinates
for i in w:
    x.append(i[0])
    y.append(i[1])
plt.plot(x, y, 'o')
plt.show()
