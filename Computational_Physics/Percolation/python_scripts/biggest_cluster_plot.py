import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import colors

import matplotlib as mpl
mpl.rcParams['svg.fonttype'] = "none"
mpl.rcParams['font.size'] = 0
mpl.rcParams['legend.numpoints'] = 1


data = np.loadtxt("../sites900000.csv", delimiter="\n")
data.astype(int)
#data = np.reshape(data, (3,3))

N = 1000
positions = np.array([None]*len(data))

mat = np.zeros((N,N), dtype=np.uint8)

def makeLattice():
    for i in range(0,len(data)):
        x = int(data[i]/N)
        y = int(data[i]%N)
        mat[x,y] = 1
makeLattice()



color = ['black', '#7FFF00']

cmap = mpl.colors.ListedColormap(color)
plt.matshow(mat, cmap=cmap)
plt.axis('off')
plt.show()

#plt.imshow(data)
#plt.show()
#plt.plot(data)
#plt.show()
