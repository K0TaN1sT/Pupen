import matplotlib.pyplot as plt   
import numpy as np

x = np.linspace(1, 10, 2)
X, X1 = np.meshgrid(x, x)
_, X2 = np.meshgrid(x, x)

# X, X1 = [[1, 2, 1, 1], [2,2, 1, 2]], [[2, 1, 1, 1], [2, 2, 2, 1]]

print(X, X1, X2, sep='\n')
plt.contour(X, X1, X2)
plt.show()