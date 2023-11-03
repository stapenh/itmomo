import numpy as np
import matplotlib.pyplot as plt



x = np.linspace(-2 * np.pi, 2 * np.pi, 100)


y = np.sin(x)


plt.plot(x, y)

plt.xlim(-np.pi, np.pi)
plt.ylim(-1, 1)


plt.xticks(np.arange(-np.pi, np.pi + np.pi/4, np.pi/4))
plt.yticks(np.arange(-1, 1.1, 0.2))

plt.grid(True)
plt.show()
