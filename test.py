import numpy as np
import matplotlib.pyplot as plt


x1 = np.linspace(0,10,20)
x2 = np.linspace(0,10,500)

y1 = np.sin(x1)
y2 = np.sin(x2)

plt.plot(x2,y2, color = 'b', zorder=0)
plt.scatter(x1,y1,marker = 'o', s = 6, color = 'r', zorder=1)

plt.show()