import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(1, 10, 100)
plt.subplot(2, 2, 1)
plt.plot(x, np.sin(x))
plt.subplot(2, 2, 3)
plt.plot(x, np.cos(x))
plt.show()