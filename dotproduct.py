import numpy as np


inputs = [1, 2, 3,2.5]
weights = [0.2, 0.8, -0.5,1.0]
bias = 2

weights2 = [0.5, -0.91, 0.26, -0.5]
bias2 = 3

weights3 = [-0.26, -0.27, 0.17, 0.87]
bias3 = 0.5


weights = [[0.2, 0.8, -0.5,1.0],[0.5,-0.91,0.26,-0.5],[-0.26, -0.27, 0.17, 0.87]]
biases = [2,3,0.5]


output = np.dot(weights,inputs) +biases  ## first argument must be weights
print(output)

layer_outputs = []





