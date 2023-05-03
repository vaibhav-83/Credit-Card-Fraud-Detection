import numpy as np

m, n, data, desired_outputs = 0, 0, [], []

with open('creditcard 1000 entries.csv') as f:
    while True:
        inp = f.readline().strip()
        if inp is '': break
        inp = inp.split(',')
        m, n = m+1, len(inp)
        for i in range(0, n): inp[i] = float(inp[i])
        desired_outputs.append(inp[n-1])
        inp[n-1] = 1
        data.append(inp)

train, test, weights, no_of_iterations, c = 600, 536, [], 45, 0.3

with open('Init_weights.txt') as f:
    weights = f.readline().strip().split(',')
    for i in range(0, n): weights[i] = float(weights[i])

def signum(some_output):
    if some_output >= 0: return 1
    else: return 0

for j in range(0, no_of_iterations):
    for i in range(0, train):
        net = np.matmul(weights, np.transpose(data[i]))
        actual_output = signum(net)
        if(actual_output != desired_outputs[i]):
            weights = np.add(weights, np.multiply(float(c*(desired_outputs[i]-actual_output)), data[i]))
    c -= 0.01*c

for i in range(0, n):
    if i<n-1: print(weights[i],end=',')
    else: print(weights[i])