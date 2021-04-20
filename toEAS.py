import pickle
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

WIDTH = 416
HEIGHT = 300

N_NEIGH_EDGE = 6
BMP_TRESH = 128

def sum_around3x3(bmp, x, y):
    return sum([bmp[Y][X] for Y in range(y-1,y+2) for X in range(x-1,x+2)])

def isedge(bmp, x, y):
    return bmp[y][x] == 1 and sum_around3x3(bmp, x, y) == N_NEIGH_EDGE

def euclidianSquared(a,b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2

def findNearest(p, coords):
    n = coords[0]
    min = euclidianSquared(p,n)

    for c in coords:
        dist = euclidianSquared(p,c)
        if dist < min:
            min = dist
            n = c
    return n

def squarePath(a,b,order=0):
    if order==0:
        p = (a[0], b[1])
    else:
        p = (b[0], a[1])

    return [a, p, b]

def linearPath(a,b):
    x = a[0]
    y = a[1]

    stepx = 
    stepy = 

with Image.open("testframe.png") as im:
    red = [[im.getpixel((x, y))[0] for x in range(im.width)] for y in range(im.height)]

bitmap = [[0 if red[y][x] < BMP_TRESH else 1 for x in range(im.width)] for y in range(im.height)]

edges_coord = []
for x in range(1, im.width - 1):
    for y in range(1, im.height - 1):
        if isedge(bitmap, x, y):
            edges_coord.append((x,y))

#creation du path

path = []

n = edges_coord[0]
edges_coord.remove(n)
while len(edges_coord) != 0:
    n2 = findNearest(n,edges_coord)

    path.extend(squarePath(n, n2))

    edges_coord.remove(n2)
    n = n2

edges_bmp = [[isedge(bitmap, x, y) for x in range(1, im.width - 1)] for y in range(1, im.height - 1)]
plt.imshow(edges_bmp)
plt.show()

clean = []
path_clean = list(dict.fromkeys(path))
for c in path_clean:
    if c[0] != 1:
        clean.append(c)

print(clean)

with open('test.eas', 'wb') as handle:
     pickle.dump(clean, handle, protocol=pickle.HIGHEST_PROTOCOL)
