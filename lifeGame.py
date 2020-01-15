import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

n = int(input('세포세계의 크기를 입력하세요 : '))
world = np.zeros((n, n))

def get_alive():
    location = input('''살아있을 1세대 세포의 위치를 입력하시오: ''')
    x, y = map(int, location.split())
    world[x][y] = 1

def cell_con(x,y):
    count = 0
    for i in range(max(x-1, 0), min(x+1, n)):
        for j in range(max(y-1, 0), min(y+1, n)):
            count += world[i][j]
            count = count - world[x][y]
    if count == 3:
        world[x][y] = 1
    elif count == 2:
        pass
    else:
        world[x][y] = 0

def next_gen():
    next_world = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            cell_con(i,j)
    np.full((n,n), world)


get_alive()
print()


#plt.imshow(world, cmap = 'binary')
#plt.show()













