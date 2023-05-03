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

weights=[]
with open('final_weights.txt') as f:
    weights = f.readline().strip().split(',')
    for i in range(0, n): weights[i] = float(weights[i])

train, test, no_of_correct_predictions = 600, 536, 0

def signum(some_output):
    if some_output > 0: return 1
    else: return 0

for i in range(train, train+test):
    net = np.matmul(weights, np.transpose(data[i]))
    actual_output = signum(net)
    if actual_output == desired_outputs[i]:
        no_of_correct_predictions += 1

print("Total Correct: "+str(no_of_correct_predictions))
accuracy = float(no_of_correct_predictions/test * 100)
print("Accuracy: {0}%".format(accuracy))