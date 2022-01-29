
inputs = [1, 2, 3,2.5]
weights = [0.2, 0.8, -0.5,1.0]
bias = 2

weights2 = [0.5, -0.91, 0.26, -0.5]
bias2 = 3

weights3 = [-0.26, -0.27, 0.17, 0.87]
bias3 = 0.5





output = inputs[0]*weights[0] + inputs[1]*weights[1] + inputs[2]*weights[2] + inputs[3]*weights[3] + bias


output2 = inputs[0]*weights2[0] + inputs[1]*weights2[1] + inputs[2]*weights2[2] + inputs[3]*weights2[3] + bias2


output3 = inputs[0]*weights3[0] + inputs[1]*weights3[1] + inputs[2]*weights3[2] + inputs[3]*weights3[3] + bias3


print("First neuron output: " + str(output) + "\n" + "Second neuron output: " + str(output2) + "\n" + "Third neuron output: " + str(output3))


